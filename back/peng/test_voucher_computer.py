import unittest

from main import VoucherComputer


class VoucherTestCase(unittest.TestCase):
    """
    Basic test over simple functions
    """

    def setUp(self):
        self.vc = VoucherComputer()
        self.vouchers = [
            {
                "country_code": "us",
                "coupon_id": 259887,
                "coupon_webshop_name": "Macy's  & Promo Codes",
                "description": "25% OFF Sale Save 25% Off Petite Tops 50 uses today Get Deal See Details Details Add a Comment Ends:  Today Details:  Get 25% Off Petite Tops! Find your perfect sleeve length without worrying about hemming. Include nearby city with my comment to help other users. Post Comment Comment Posted Post Another Comment",
                "first_seen": "2017-09-06",
                "last_seen": "2017-09-06",
                "promotion_type": "percent-off",
                "title": "25% Off Petite Tops",
                "value": 25,
                "webshop_id": "macys"
            },
            {
                "country_code": "us",
                "coupon_id": 215688,
                "coupon_webshop_name": "Nordstrom  & Promo Codes",
                "description": "Free Gift Save Show Coupon Code 8 uses today Free Gentle Foaming Cleanser & Cosmetics Bag With Clarins Purchase of $75 Details: Get Free Gentle Foaming Cleanser with cottonseed, Multi-Active Night Cream and Cosmetics Bag with Clarins purchase of $75. 100% Success 100% Success Add a Comment Include nearby city with my comment to help other users. Post Comment Comment Posted Post Another Comment",
                "first_seen": "2017-05-05",
                "last_seen": "2017-09-07",
                "promotion_type": "dollar-off",
                "title": "Free Gentle Foaming Cleanser & Cosmetics Bag With Clarins Purchase of $75",
                "value": 75,
                "webshop_id": "nordstrom"
            },
        ]
        self.vouchers_with_none_values = [
            {
                "country_code": "us",
                "coupon_id": 259887,
                "coupon_webshop_name": "Macy's  & Promo Codes",
                "description": "25% OFF Sale Save 25% Off Petite Tops 50 uses today Get Deal See Details Details Add a Comment Ends:  Today Details:  Get 25% Off Petite Tops! Find your perfect sleeve length without worrying about hemming. Include nearby city with my comment to help other users. Post Comment Comment Posted Post Another Comment",
                "first_seen": "2017-09-06",
                "last_seen": "2017-09-06",
                "promotion_type": "percent-off",
                "title": "25% Off Petite Tops",
                "value": 25,
                "webshop_id": "macys"
            },
            {
                "country_code": "us",
                "coupon_id": 252399,
                "coupon_webshop_name": "Nordstrom  & Promo Codes",
                "description": "FREE GIFT Sale Save Free Pouch & Deluxe Samples & Body Creme With $100 Jo Malone London Orders Get Deal See Details Details Add a Comment Details:  Receive a drawstring pouch and deluxe samples of Basil & Neroli Cologne (0.3 oz.), Wood Sage & Sea Salt Body & Hand Wash (0.5 oz.) and English Pear & Freesia Body Crème (0.5 oz.) with your $100 Jo Malone London purchase. Online only. Include nearby city with my comment to help other users. Post Comment Comment Posted Post Another Comment",
                "first_seen": "2017-08-10",
                "last_seen": "2017-09-07",
                "promotion_type": None,
                "title": "Free Pouch & Deluxe Samples & Body Creme With $100 Jo Malone London Orders",
                "value": None,
                "webshop_id": "nordstrom"
            },
        ]
        self.promotion_type = "percent-off"

    def test_count_types(self):
        result = self.vc.count_types(self.vouchers)
        self.assertEqual(result, {'dollar-off': 1, 'percent-off': 1}, "Should be '{'dollar-off': 1, 'percent-off': 1}'")

    def test_count_types_empty_param(self):
        result = self.vc.count_types([])
        self.assertEqual(result, {}, "Should be '{}'")

    def test_count_types_no_param(self):
        with self.assertRaises(TypeError):
            result = self.vc.count_types()

    def test_get_promotion_vouchers(self):
        result = self.vc.get_promotion_vouchers(self.vouchers, self.promotion_type)
        self.assertEqual(result, [
            {'country_code': 'us', 'coupon_id': 259887, 'coupon_webshop_name': "Macy's  & Promo Codes",
             'description': '25% OFF Sale Save 25% Off Petite Tops 50 uses today Get Deal See Details Details Add a Comment Ends: \xa0Today Details: \xa0Get 25% Off Petite Tops! Find your perfect sleeve length without worrying about hemming. Include nearby city with my comment to help other users. Post Comment Comment Posted Post Another Comment',
             'first_seen': '2017-09-06', 'last_seen': '2017-09-06', 'promotion_type': 'percent-off',
             'title': '25% Off Petite Tops', 'value': 25, 'webshop_id': 'macys'}])

    def test_get_promotion_vouchers_empty_param(self):
        result = self.vc.get_promotion_vouchers([], "")
        self.assertEqual(result, [])

    def test_get_promotion_vouchers_no_param(self):
        with self.assertRaises(TypeError):
            result = self.vc.get_promotion_vouchers()

    def test_get_promotion_vouchers_wrong_type_param(self):
        with self.assertRaises(TypeError):
            result = self.vc.count_types("foo", True)

    def test_get_get_min_max_avg(self):
        result = self.vc.get_min_max_avg(self.vouchers)
        self.assertEqual(result, {'max': 75, 'min': 25, 'avg': 50.0, 'values': {25: 1, 75: 1}})

    def test_get_min_max_avg_with_none_values(self):
        with self.assertRaises(TypeError):
            result = self.vc.get_min_max_avg(self.vouchers_with_none_values)

    def test_get_min_max_avg_empty_param(self):
        with self.assertRaises(ValueError):
            result = self.vc.get_min_max_avg([])

    def test_get_min_max_avg_no_param(self):
        with self.assertRaises(TypeError):
            result = self.vc.get_min_max_avg()

    def test_get_min_max_avg_wrong_type_param(self):
        with self.assertRaises(TypeError):
            result = self.vc.get_min_max_avg(True)


if __name__ == '__main__':
    unittest.main()
