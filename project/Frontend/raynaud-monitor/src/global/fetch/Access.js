import { BASE_URI } from '@/global/Variables'
import router from '@/router'

import store from '@/store'

//import Episodes from same folder
import Episodes from './Episodes'

export default {
    async login(email, password) {

        const response = await fetch(`${BASE_URI}/login`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ email, password }),
        })

        if (response.status === 200) {
            const body = await response.json()
            const expires = new Date().getTime() + body.session_expires * 1000 * 60

            localStorage.setItem('token', body.access_token)
            localStorage.setItem('sessionExpires', expires )

            // Set timeout for session expiration
            setTimeout(() => {
                localStorage.removeItem('token')
                localStorage.removeItem('sessionExpires')
                router.push('/login')
            }, expires - new Date().getTime())

            const episodes = await Episodes.getAll()
            store.commit('setEpisodes', episodes)
            
            return 0
        }

        return -1
    },
    logout() {
        localStorage.removeItem('token')
        localStorage.removeItem('sessionExpires')
        localStorage.removeItem('user')
        if (router.app._route.path !== '/login') router.push({ path: '/login' })
    },
    async me() {
        const response = await fetch(`${BASE_URI}/users/me`, {
            method: 'GET',
            headers: {'Content-Type': 'application/json', 'Authorization': `Bearer ${localStorage.getItem('token')}`},
        })

        if (response.status === 200) {
            const body = await response.json()
            localStorage.setItem('user', JSON.stringify(body))
            return body
        }

        return -1
    },
    async register(email, password) {
            
        const response = await fetch(`${BASE_URI}/users`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ email, password }),
        })

        if (response.status === 200) {
            return 0
        }

        return -1
    }
} 