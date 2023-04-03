<template>
  <div class="list">
    <ul>
      <li v-for="cat in data" :key="cat.id" @click="selectImage(cat)">
        {{ cat.breeds[0].name }}
      </li>
    </ul>
  </div>

  <div class="image">
    <div class="image-container" ref="bar">
      <span v-if="!catSelected" class="welcome-text">Click on a name to show details</span>

      <div v-else class="image-content">
        <img
          :style="{
            height: catSelected.height + 'px',
            backgroundImage: 'url(' + catSelected.url + ')'
          }"
          alt=""
          @click="increaseCounter"
        />

        <div class="image-content-text-container">
          <span>
            {{ catSelected.breeds[0].description }}
          </span>

          <span>Origin&nbsp;: {{ catSelected.breeds[0].origin }}</span>
          <span>Clicks&nbsp;: {{ catSelected.clicks }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      data: [],
      catSelected: null
    }
  },
  methods: {
    selectImage(cat) {
      this.catSelected = cat
      this.scrollTo()
    },
    increaseCounter() {
      this.catSelected.clicks += 1
    },
    hydrateData() {
      this.data.map((itm) => {
        itm.clicks = 0
      })
    },
    scrollTo() {
      console.log(this.$refs)
      this.$nextTick(() => this.$refs.bar.scrollIntoView({ behavior: 'smooth' }))
    }
  },

  mounted() {
    const apiKey = import.meta.env.VITE_API_KEY
    const limitNumber = 10
    const breedIds = 'beng,mcoo,sphy'
    const apiUrl = 'https://api.thecatapi.com/v1/images/search?'

    fetch(`${apiUrl}limit=${limitNumber}&breed_ids=${breedIds}&api_key=${apiKey}`).then(
      async (response) => {
        const jsonData = await response.json()
        this.data = jsonData
        this.hydrateData()
      }
    )
  }
}
</script>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.list ul {
  list-style: none;
}

.list ul li {
  border: 1px solid white;
  border-radius: 20px;
  padding: 10px;
  width: 300px;
  cursor: pointer;
  text-align: center;
  margin: 10px;
}

.list ul :first-child {
  margin-top: unset;
}

.list ul :last-child {
  margin-bottom: unset;
}

.image-container {
  border: 1px solid white;
  height: 600px;
  width: 500px;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;

  flex-direction: column;
}

.image-content-text-container {
  padding: 20px;
  display: flex;
  flex-direction: column;
}

.image-content-text-container :first-child {
  margin-top: 0;
}

.image-content-text-container span {
  margin-top: 10px;
}

.image {
  display: flex;
  align-items: center;
}

.image-content {
  height: 100%;
  width: 100%;

  display: flex;
  flex-direction: column;
}

.image-content img {
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center;
  width: 100%;
  cursor: pointer;
}

@media (max-width: 1024px) {
  .list {
    display: flex;
    justify-content: center;
    padding: 20px;
  }

  .list ul {
    padding: unset;
  }

  .image {
    display: flex;
    justify-content: center;
    padding: 20px;
  }
}
</style>
