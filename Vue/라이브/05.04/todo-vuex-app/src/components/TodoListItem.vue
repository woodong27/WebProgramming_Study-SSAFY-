<template>
    <div>
        <div>{{ todoItem.title }}</div>
    </div>
</template>

<script>
export default {
    name: 'TodoListItem',
    props: {
        todoItem: Object,
    }
}
</script>

<style>

</style>