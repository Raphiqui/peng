import json
import pprint
from collections import Counter
from itertools import groupby
from os import path

import plotly.graph_objects as go

PROMOTION_TYPES = ["percent-off", "dollar-off"]


class VoucherComputer:
    """
    This class aims to read a 'database' from a json format file then applies some computation on it
    at the end the computation must be generated in a way to be shown with plotly.
    """

    def __init__(self) -> None:
        self.vouchers = self._parse_file()
        self.macys_vouchers = []
        self.nike_vouchers = []
        self.nordstrom_voucher = []

    def __setitem__(self, key, new_value):
        if key == "macys" and new_value is not None:
            self.macys_vouchers = new_value

        if key == "nike" and new_value is not None:
            self.nike_vouchers = new_value

        if key == "nordstrom" and new_value is not None:
            self.nordstrom_voucher = new_value

    @classmethod
    def _parse_file(cls) -> dict:
        """
        Reads a specified file and returns it as a json
        """
        file_path = path.join(path.dirname(__file__), "coupons.json")

        with open(file_path, encoding="utf-8", mode="r") as f:
            data = json.load(f)
            return data

    def order_by_retailers(self) -> None:
        """
        According to the documentation of `groupby` itertools, the iterable needs to already be sorted on the same key
        function.

        Then it'll retrieve and gather all objects corresponding to a key.

        Again, according to the documentation, each iteration will make unavailable the previous iterable which (as needed)
        is stored as a list.
        """

        coupon_by_retailers = sorted(self.vouchers["coupons"], key=self.key_func)

        for key, value in groupby(coupon_by_retailers, self.key_func):
            self[f"{key}"] = list(value)

    def statistic_computations(self, vouchers: []) -> {}:
        """
        All the statistic operations gather in one place

        :return: object regarding the results of all computation processes
        """

        types_count = self.count_types(vouchers)
        percent_off_vouchers = self.get_promotion_vouchers(vouchers, PROMOTION_TYPES[0])
        dollar_off_vouchers = self.get_promotion_vouchers(vouchers, PROMOTION_TYPES[1])

        percent_min_max_avg = self.get_min_max_avg(percent_off_vouchers)
        dollar_min_max_avg = self.get_min_max_avg(dollar_off_vouchers)

        return {
            "types_count": types_count,
            "percent_off_vouchers": percent_off_vouchers,
            "dollar_off_vouchers": dollar_off_vouchers,
            "percent_min_max_avg": percent_min_max_avg,
            "dollar_min_max_avg": dollar_min_max_avg,
        }

    @staticmethod
    def count_types(vouchers: []) -> {}:
        """
        Counter is collection which provides an easy way to count occurrences of value
        It'll return a Counter object

        :return: dictionary containing {'key found': 'number of occurrences', ...}
        """
        return dict(Counter((x['promotion_type']) for x in vouchers))

    @staticmethod
    def get_promotion_vouchers(vouchers: [], promotion_type: str) -> []:
        """
        List comprehension as we wanted a list in return

        :return: list with item corresponding to promotion type
        """
        return [itm for itm in vouchers if itm["promotion_type"] == promotion_type]

    @staticmethod
    def get_min_max_avg(vouchers: []) -> {}:
        """
        Computation over values to return a statistic object which aims to be shown
        """
        values = [itm["value"] for itm in vouchers]

        return {
            "max": max(values),
            "min": min(values),
            "avg": round(sum(values) / len(values), 2),
            "values": dict(Counter(values)),
        }

    @classmethod
    def key_func(cls, k):
        """
        Custom key function specified into the declaration of `sorted`
        Util to know by which key the data will be sorted
        """
        return k['webshop_id']

    @staticmethod
    def plot_statistics(data: dict, title: str, xaxis_title: str, yaxis_title: str) -> None:
        x_values = list(data["values"].values())
        y_values = list(data["values"].keys())
        avg = data["avg"]

        max_val = max(y_values)
        max_key = x_values[y_values.index(max_val)]
        min_val = min(y_values)
        min_key = x_values[y_values.index(min_val)]

        # Create scatter plots with markers for maximum and minimum values of x and y
        x_max = go.Scatter(x=[max_key], y=[max_val], mode="markers", name=f"Max ({max_key}, {max_val})",
                           marker=dict(color="red", size=10, symbol="star"))
        x_min = go.Scatter(x=[min_key], y=[min_val], mode="markers", name=f"Min ({min_key}, {min_val})",
                           marker=dict(color="blue", size=10, symbol="bowtie"))

        # Create a horizontal line for the avg value
        avg_line = go.Scatter(x=[min(x_values), max(x_values)], y=[avg, avg], mode='lines',
                              name=f'Average ({avg:.2f})', line=dict(color='green', width=2, dash='dash'))

        plot = go.Figure(
            data=[go.Scatter(x=x_values, y=y_values, mode="markers", name="Values"), x_max, x_min, avg_line],
        )

        plot.update_layout(title=title, xaxis_title=xaxis_title, yaxis_title=yaxis_title)

        # Open browser with localhost to show graph
        plot.show()


if __name__ == "__main__":
    """
    Simple examples of all the computation process
    """

    vc = VoucherComputer()
    vc.order_by_retailers()

    general = vc.statistic_computations(vc.vouchers["coupons"])
    macys = vc.statistic_computations(vc.macys_vouchers)
    nike = vc.statistic_computations(vc.nike_vouchers)
    nordstrom = vc.statistic_computations(vc.nordstrom_voucher)

    xaxis_title = "Voucher number"
    percent_off_title = "Percent off (%)"
    dollar_off_title = "Dollar off ($)"

    vc.plot_statistics(
        data=general["dollar_min_max_avg"],
        title="Dollar off via voucher number (General)",
        xaxis_title=xaxis_title,
        yaxis_title=dollar_off_title,
    )

    vc.plot_statistics(
        data=general["percent_min_max_avg"],
        title="Percent off via voucher number (General)",
        xaxis_title=xaxis_title,
        yaxis_title=percent_off_title,
    )

    vc.plot_statistics(
        data=macys["dollar_min_max_avg"],
        title="Dollar off via voucher number (Macys)",
        xaxis_title=xaxis_title,
        yaxis_title=dollar_off_title,
    )

    vc.plot_statistics(
        data=macys["percent_min_max_avg"],
        title="Percent off via voucher number (Macys)",
        xaxis_title=xaxis_title,
        yaxis_title=percent_off_title,
    )

    vc.plot_statistics(
        data=nike["dollar_min_max_avg"],
        title="Dollar off via voucher number (Nike)",
        xaxis_title=xaxis_title,
        yaxis_title=dollar_off_title,
    )

    vc.plot_statistics(
        data=nike["percent_min_max_avg"],
        title="Percent off via voucher number (Nike)",
        xaxis_title=xaxis_title,
        yaxis_title=percent_off_title,
    )

    vc.plot_statistics(
        data=nordstrom["dollar_min_max_avg"],
        title="Dollar off via voucher number (NordStorm)",
        xaxis_title=xaxis_title,
        yaxis_title=dollar_off_title,
    )

    vc.plot_statistics(
        data=nordstrom["percent_min_max_avg"],
        title="Percent off via voucher number (NordStorm)",
        xaxis_title=xaxis_title,
        yaxis_title=percent_off_title,
    )