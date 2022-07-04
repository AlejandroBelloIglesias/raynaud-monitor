const Formatter = {
    format: (time) => {
        if (time === undefined || time === null)
            return ''

        if (typeof time === 'string')
            time = Number.parseInt(time)

        const date = new Date(time)
        const dd = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
        const MM = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : (date.getMonth() + 1)
        const yyyy = date.getFullYear()
        const hh = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
        const mm = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()

        return `${dd}/${MM}/${yyyy} ${hh}:${mm}`
    },
    formatReversed: (time) => {
        if (time === undefined || time === null)
            return ''

        if (typeof time === 'string')
            time = Number.parseInt(time)

        const date = new Date(time)
        const dd = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
        const MM = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : (date.getMonth() + 1)
        const yyyy = date.getFullYear()
        const hh = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
        const mm = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()

        return `${hh}:${mm} - ${dd}/${MM}/${yyyy}`
    },
    formatWithSeconds: (time) => {
        if (time === undefined || time === null)
            return ''

        if (typeof time === 'string')
            time = Number.parseInt(time)

        const date = new Date(time)
        const dd = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
        const MM = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : (date.getMonth() + 1)
        const yyyy = date.getFullYear()
        const hh = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
        const mm = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()
        const ss = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds()

        return `${dd}/${MM}/${yyyy} ${hh}:${mm}:${ss}`
    },
    formatWithSecondsReversed: (time) => {
        if (time === undefined || time === null)
            return ''

        if (typeof time === 'string')
            time = Number.parseInt(time)

        const date = new Date(time)
        const dd = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
        const MM = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : (date.getMonth() + 1)
        const yyyy = date.getFullYear()
        const hh = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
        const mm = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()
        const ss = date.getSeconds() < 10 ? '0' + date.getSeconds() : date.getSeconds()

        return `${hh}:${mm}:${ss} - ${dd}/${MM}/${yyyy}`
    },
    formatHour: (time) => {
        if (time === undefined || time === null)
            return ''

        if (typeof time === 'string')
            time = Number.parseInt(time)

        const date = new Date(time)
        const hh = date.getHours() < 10 ? '0' + date.getHours() : date.getHours()
        const mm = date.getMinutes() < 10 ? '0' + date.getMinutes() : date.getMinutes()

        return `${hh}:${mm}`
    },
    formatNoHour: (time) => {
        if (time === undefined || time === null)
            return ''

        if (typeof time === 'string')
            time = Number.parseInt(time)

        const date = new Date(time)
        const dd = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
        const MM = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : (date.getMonth() + 1)
        const yyyy = date.getFullYear()

        return `${dd}/${MM}/${yyyy}`
    },
    formatNoHourWithSlash: (time) => {
        if (time === undefined || time === null)
            return ''

        if (typeof time === 'string')
            time = Number.parseInt(time)

        const date = new Date(time)
        const dd = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
        const MM = date.getMonth() + 1 < 10 ? '0' + (date.getMonth() + 1) : (date.getMonth() + 1)
        const yyyy = date.getFullYear()

        return `${dd}-${MM}-${yyyy}`
    }
}

export default Formatter