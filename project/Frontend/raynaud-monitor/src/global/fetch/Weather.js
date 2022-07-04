
const key = `85e84ad49a2127357cc16b0c8226d96b`

export default {
    async getWeather(latitude, longitude) {
        
        const url = `https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&appid=${key}`
        const response = await fetch(url)
        const body = await response.json()
        return body
    }
}
