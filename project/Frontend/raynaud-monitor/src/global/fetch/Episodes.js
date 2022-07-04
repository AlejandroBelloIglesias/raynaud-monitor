
import { BASE_URI } from '@/global/Variables'

export default {
    async getAll() {

        const response = await fetch(`${BASE_URI}/users/me/episodes`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json', 
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
        })

        if (response.status === 200) {
            const body = await response.json()
            return body
        }

        return []
    },
    async insert(episode) {
        const response = await fetch(`${BASE_URI}/users/me/episodes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', 
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify(episode)
        })

        if (response.status === 200) {
            const body = await response.json()
            return body
        }

        return null
    },
    async delete(id) {
        const response = await fetch(`${BASE_URI}/users/me/episodes/${id}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json', 
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
        })

        if (response.status === 200) {
            const body = await response.json()
            return body
        }

        return null
    },
    async modify(episode) {
        const response = await fetch(`${BASE_URI}/users/me/episodes/${episode.id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json', 
                'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: JSON.stringify(episode)
        })

        if (response.status === 200) {
            const body = await response.json()
            return body
        }

        return null
    }
}