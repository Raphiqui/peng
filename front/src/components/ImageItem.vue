<template>
  <div class="image-content">
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
</template>

<script>
export default {
  props: {
    catSelected: {
      type: Object,
      default: () => {}
    }
  },

  methods: {
    increaseCounter() {
      this.catSelected.clicks += 1
    }
  }
}
</script>

<style scoped>
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
</style>
