<script setup>
import WelcomeItem from './WelcomeItem.vue'
import ListItem from './ListItem.vue'
import ImageItem from './ImageItem.vue'
</script>

<template>
  <div class="cp">
    <ListItem :data="data" @cat-breed-selected="selectCatBreed" />

    <div class="image">
      <div class="image-container" ref="imgContainer">
        <WelcomeItem v-if="!catSelected">
          <template #heading>Click a breed to show details</template>
        </WelcomeItem>

        <ImageItem v-else :cat-selected="catSelected"/>
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
    selectCatBreed(cat) {
      this.catSelected = cat
      this.scrollTo()
    },
    hydrateData() {
      /**
       * Add key value to know how many clicks which images has
       */
      this.data.map((itm) => {
        itm.clicks = 0
      })
    },
    scrollTo() {
      /**
       * Most likely used to improve mobile experience as list is above and image is below, each time a cat breed is
       * selected the view will scroll to the result
       */
      this.$nextTick(() => this.$refs.imgContainer.scrollIntoView({ behavior: 'smooth' }))
    }
  },

  mounted() {
    // Seems that with Vue3 keys handled by dotenv must be prefixed by 'VITE_'
    const apiKey = import.meta.env.VITE_API_KEY
    const limitNumber = 10
    const breedIds = 'beng,mcoo,sphy'
    const apiUrl = import.meta.env.VITE_API_URL

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
.cp {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

.image-container {
  border: 1px solid var(--vt-c-white);
  height: 600px;
  width: 500px;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;

  flex-direction: column;
}

@media (max-width: 1024px) {
  .cp {
    flex-direction: column;
    align-items: unset;
  }

  .list {
    display: flex;
    justify-content: center;
    padding: 20px;
  }

  .image {
    display: flex;
    justify-content: center;
    padding: 20px;
  }
}
</style>
