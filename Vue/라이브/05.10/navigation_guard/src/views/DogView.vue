<template>
  <div>
    <img v-if="imgSrc" :src="imgSrc" alt="Picture of Dog"><br>
    <div v-if='!imgSrc'>{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'DogView',
    data() {
        return {
            imgSrc: null,
            message: null
        }
    },
    methods: {
        getDogImage() {
            const breed=this.$route.params.breed
            const dogImageURL=`https://dog.ceo/api/breed/${breed}/images/random`
            axios({
                method: 'get',
                url: dogImageURL
            })
            .then(response => {
                const imgSrc=response.data.message
                this.imgSrc=imgSrc
            })
            .catch(error => {
                console.log(error)
                this.message=`${this.$route.params.breed}는 없는 품종입니다.`
                this.$router.push('/404')
            })
        }
    },
    created() {
        this.getDogImage()
    }
}
</script>

<style>

</style>