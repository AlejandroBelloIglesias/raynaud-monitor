
import { BASE_URI } from '@/global/Variables'

export default {
    async getAll() {

        const response = await fetch(`${BASE_URI}/body_parts`)

        if (response.status === 200) {
            const body = await response.json()
            return body
        }

        return -1
    },
}