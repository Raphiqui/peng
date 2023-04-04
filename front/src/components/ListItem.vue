<template>
  <div class="list">
    <ul>
      <li v-for="cat in data" :key="cat.id" @click="selectCatBreed(cat)">
        {{ cat.breeds[0].name }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    data: {
      type: Array,
      default: () => []
    },
  },

  methods: {
    selectCatBreed(cat) {
      this.$emit('catBreedSelected', cat)
    }
  }
}
</script>

<style scoped>
.list ul {
  list-style: none;
  padding: unset;
}

.list ul li {
  border: 1px solid var(--vt-c-white);
  border-radius: 20px;
  padding: 10px;
  width: 300px;
  cursor: pointer;
  text-align: center;
  margin: 10px 0;
  box-sizing: border-box;
}

.list ul :first-child {
  margin-top: unset;
}

.list ul :last-child {
  margin-bottom: unset;
}

@media (max-width: 1024px) {
  .list {
    display: flex;
    justify-content: center;
    padding: 20px;
  }

  .list ul {
    max-width: 320px;
    width: 100%;
  }

  .list ul li {
    width: 100%;
  }
}
</style>
