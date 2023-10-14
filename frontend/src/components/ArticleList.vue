<!--  frontend/src/components/ArticleList.vue  -->

<template>
    <div v-for="article in info.results" v-bind:key="article.url" id="articles">
        <!-- 新增一个网格层 -->
        <div class="grid" :style="grid_style(article)">
            <div class="image-container">
                <img :src="image_if_exists(article)" alt="" class="image">
            </div>
            <div>
                <span v-if="article.category !== null" class="category">
                    {{ article.category.title }}
                </span>
                <span v-for="tag in article.tags" v-bind:key="tag" class="tag">
                    {{ tag }}
                </span>
            </div>

            <router-link :to="{ name: 'ArticleDetail', params: { id: article.id } }" class="article-title">
                {{ article.title }}
            </router-link>

            <div>{{ formatted_time(article.created) }}</div>
        </div>
    </div>

    <div id="paginator">
        <span v-if="is_page_exists('previous')">
            <router-link :to="get_path('previous')">
                Prev
            </router-link>
        </span>
        <span class="current-page">
            {{ get_page_param('current') }}
        </span>
        <span v-if="is_page_exists('next')">
            <router-link :to="get_path('next')">
                Next
            </router-link>
        </span>
    </div>
</template>

<script>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
import getArticleData from '@/composables/getArticleData.js'
import pagination from '@/composables/pagination.js'
import articleGrid from '@/composables/articleGrid.js'
import formattedTime from '@/composables/formattedTime.js'

export default {
    name: 'ArticleList',
    setup() {
        const info = ref('');
        // 创建路由
        const route = useRoute();
        // 获取文章列表数据的方法
        getArticleData(info, route);
        const {
            is_page_exists,
            get_page_param,
            get_path
        } = pagination(info, route);

        const {
            image_if_exists,
            grid_style
        } = articleGrid();

        // 日期格式化
        const formatted_time = formattedTime;
        // 需要注入到 Vue 实例的数据、方法等

        return {
            info,
            is_page_exists,
            get_page_param,
            get_path,
            image_if_exists,
            grid_style,
            formatted_time,
        }
    },
}

</script>

<!-- "scoped" 使样式仅在当前组件生效 -->
<style scoped>
#articles {
    padding: 10px;
}

#paginator {
    text-align: center;
    padding-top: 50px;
}

a {
    color: black;
}

.category {
    padding: 5px 10px 5px 10px;
    margin: 5px 5px 5px 0;
    font-family: Georgia, Arial, sans-serif;
    font-size: small;
    background-color: darkred;
    color: whitesmoke;
    border-radius: 15px;
}

.current-page {
    font-size: x-large;
    font-weight: bold;
    padding-left: 10px;
    padding-right: 10px;
}

.article-title {
    font-size: large;
    font-weight: bolder;
    color: black;
    text-decoration: none;
    padding: 5px 0 5px 0;
}

.tag {
    padding: 2px 5px 2px 5px;
    margin: 5px 5px 5px 0;
    font-family: Georgia, Arial, sans-serif;
    font-size: small;
    background-color: #4e4e4e;
    color: whitesmoke;
    border-radius: 5px;
}

.image {
    width: 180px;
    border-radius: 10px;
    box-shadow: darkslategrey 0 0 12px;
}

.image-container {
    width: 200px;
}

.grid {
    padding-bottom: 10px;
}
</style>