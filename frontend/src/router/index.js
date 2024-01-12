import {createRouter, createWebHistory} from "vue-router";
import Home from "@/views/Home.vue";
import LoginForm from "@/views/LoginForm.vue";
import DonationView from "@/views/DonationView.vue";
import TermsOfUseView from "@/views/TermsOfUseView.vue";

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/login',
        name: 'login',
        component: LoginForm
    },
    {
        path: '/donate',
        name: 'donate',
        component: DonationView
    },
    {
        path: '/termsofuse',
        name: 'termsofuse',
        component: TermsOfUseView
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes
});

export default router;