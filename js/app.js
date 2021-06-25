class Gallery {
    constructor(config) {
        this.container = document.querySelector(config.container);
        this.items = this.container.querySelectorAll(config.item);
        this.lightbox = this.container.querySelector(config.lightbox);
        this.modal = this.lightbox.querySelector(config.modal);
        this.config = config;
        this.addCustomAttribute();
        this.initEventListener();
    }

    addCustomAttribute() {
        let next = 0;
        let back = 0;
        for(let i = 0; i < this.items.length; i++) {
            next = i + 1;
            back = i - 1;
            // Caso especial del último item
            if (i === this.items.length - 1) {
                next = 0;
            }
            // Caso especial del primer item
            if (i === 0) {
                back = this.items.length - 1;
            }
            this.items[i].setAttribute('data-next_item', next);
            this.items[i].setAttribute('data-back_item', back);
        }
    }

    initEventListener() {
        this.items.forEach(item => {
            item.addEventListener('click', () => {
                let img = this.getImg(item);
                this.showLightbox(img.getAttribute('src'), item.dataset.next_item, item.dataset.back_item);
            });
        });

        this.modal.addEventListener('click', (e) => {
            let element = e.target;
            if (element.classList.contains(this.config.controls.back)) {
                this.changeImg(false);
            } else if (element.classList.contains(this.config.controls.next)) {
                this.changeImg(true);
            } else if (element.classList.contains(this.config.controls.close)) {
                this.lightbox.classList.remove(this.config.showLightbox);
            }
        });
    }

    getImg(item) {
        return item.querySelector(this.config.galleryImgClass);
    }

    showLightbox(imgSrc, nextItem, backItem) {
        this.lightbox.classList.add(this.config.showLightbox);
        this.addImgModal(imgSrc, nextItem, backItem);
    }

    addImgModal(imgSrc, nextItem, backItem) {
        this.modal.setAttribute('data-next_item', nextItem);
        this.modal.setAttribute('data-back_item', backItem);
        let imgModal = this.modal.querySelector(this.config.modalImgClass);
        imgModal.setAttribute('src', imgSrc);
    }

    changeImg(isNext) {
        let indexItem = this.modal.dataset.back_item;
        if (isNext) {
            indexItem = this.modal.dataset.next_item;
        }
        let item = this.items[indexItem];
        let img = this.getImg(item);
        this.addImgModal(img.getAttribute('src'), item.dataset.next_item, item.dataset.back_item);
    }
}

new Gallery({
    container: '.gallery',
    item: '.gallery__item',
    galleryImgClass: '.gallery__img',
    lightbox: '.gallery-lightbox',
    showLightbox: 'show',
    modal: '.gallery-lightbox__modal',
    modalImgClass: '.gallery-lightbox__img',
    controls: {close: 'icon-close', next: 'icon-next', back: 'icon-back'}
});
