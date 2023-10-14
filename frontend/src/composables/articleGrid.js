export default function articleGrid() {
    const image_if_exists = (article) => {
        return _imageIfExists(article)
    };

    const grid_style = (article) => {
        return _gridStyle(article)
    };
    
    return {
        image_if_exists,
        grid_style,
    }
}

function _imageIfExists(article) {
    if (article.avatar) {
        return article.avatar.content
    }
}

function _gridStyle(article) {
    if (article.avatar) {
        return {
            display: 'grid',
            gridTemplateColumns: '1fr 4fr'
        }
    }
}