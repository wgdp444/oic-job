<template>
    <transition name="modal">
        <div class="overlay" @click="$emit('close')">
            <div class="panel" @click.stop>
                <v-container>
                <v-row>
                    <v-col cols="12" sm="12" md="12" align="center">
                        <h2>本当に削除しますか？</h2>
                    </v-col>
                </v-row>
                <v-row class="mt-10">
                    <v-col cols="12" sm="1" md="1" align="center" class="offset-1">
                        <v-btn @click="$emit('close')" width="80%" color="#fcfcfc" x-medium style="font-weight: bold">いいえ</v-btn>
                    </v-col>
                    <v-col cols="12" sm="1" md="1" align="center" class="offset-5">
                        <v-btn @click="(data) => { $router.push(`/`) }" width="80%" color="#F50057" x-medium style="color: white; font-weight: bold">はい</v-btn>
                    </v-col>
                </v-row>
                </v-container>
            </div>
        </div>
    </transition>
</template>
<style lang="scss">
.overlay {
    background: rgba(0, 0, 0, .8);
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    z-index: 900;
    transition: all .5s ease;
}
 
.panel {
    width: 300px;
    height: 200px;
    background: #fff;
    padding: 20px;
    position: absolute;
    left: 50%;
    top: 50%;
    margin-left: -150px;
    margin-top: -100px;
    transition: all .3s ease;
}
.modal-enter,
.modal-leave-active {
    opacity: 0;
}
 
.modal-enter .panel,
.modal-leave-active .panel{
    top: -200px;
}
</style>
