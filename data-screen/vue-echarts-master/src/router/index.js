import Vue from 'vue'
import Router from 'vue-router'
import home from '@/views/home';
import areaChart from "@/views/components/EverydayConsume";

Vue.use(Router)

const router = new Router({
    routes: [
        {
            path: '/',
            redirect: '/page'
        },
        {
            path: '',
            name: 'home',
            component: home,
            children: [
                {
                    path: '/page',
                    name: 'page',
                    component: () => import('@/views/page'),
                    children: [
                        {
                            path: '/areaChart',
                            name: 'areaChart',
                            component: areaChart,
                            props: (route) => ({
                                selectRangeDate: route.query.selectRangeDate,
                                config: route.query.config
                            })

                        },]
                },
            ]
        }
    ]
})
export default router