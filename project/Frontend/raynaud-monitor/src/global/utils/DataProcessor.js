const DataProcessor = {
    yearSummaryByMonth(episodes, year) {
        if (episodes.length === 0) {
            return [];
        }
        const yearSummary = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        episodes.forEach(episode => {
            const date = new Date(episode.date_time)
            if (date.getFullYear() === year) {
                const month = date.getMonth()
                if (yearSummary[month]) {
                    yearSummary[month] += 1
                } else {
                    yearSummary[month] = 1
                }
            }
        });
        return yearSummary;
    },
    monthSummaryByDay(episodes, month) {
        if (episodes.length === 0) {
            return [];
        }
        // Get month number of days
        const monthDays = new Date(new Date().getFullYear(), month + 1, 0).getDate();
        let monthSummary = [];
        for (let i = 0; i < monthDays; i++) {
            monthSummary.push(0);
        }
        episodes.forEach(episode => {
            const date = new Date(episode.date_time)
            if (date.getMonth() === month) {
                const day = date.getDate()
                monthSummary[day - 1] += 1
            }
        });
        return monthSummary;
    },
    episodesByTemperature(episodes) {
        if (episodes.length === 0) {
            return [];
        }
        // Get min and max temperature first
        const minTemp = episodes.reduce((min, episode) => {
            return episode.temperature < min ? episode.temperature : min
        }
            , episodes[0].temperature)
        const maxTemp = episodes.reduce((max, episode) => {
            return episode.temperature > max ? episode.temperature : max
        }
            , episodes[0].temperature)

        // Create and fill array with every temperature from min to max
        const temperatures = []
        for (let i = 0; i <= (maxTemp - minTemp); i++) {
            temperatures.push({temp: minTemp + i, episodes: []})
        }
        // Fill array with episodes
        episodes.forEach(episode => {
            const index = temperatures.findIndex(temp => temp.temp === episode.temperature)
            temperatures[index].episodes.push(episode)
        }, temperatures)
            
        return temperatures
    },
    parabolaRandom(middle) {
        let x = Math.floor(middle * (Math.pow(Math.random(), 0.5)))
        if (Math.random() < 0.5) 
            x = middle - x
        else
            x = middle + x;
        return x
    },
    parabolaRandom2(middle) {
        let x = Math.floor(middle * (Math.pow(Math.random(), 0.5)))
        if (Math.random()) 
            x = middle - x;
        return x
    },
    demoData() {
        const user_id = 0;
        let episodes = []

        for (let i = 0; i < 200; i++) {
            
            //Random date in current year using parabola
            let date_time = new Date(new Date().getFullYear(), 0, 0)
            date_time.setDate(date_time.getDate() + this.parabolaRandom((366/2)+30))

            //Random duration between 1 and 40 minutes (integer)
            let duration = Math.floor(Math.random() * 40) + 1;
            
            //Random temperature between -10 and 25 degrees (integer) (Less has more chance to happen)
            let temperature = Math.floor(this.parabolaRandom2(30) -10)

            //Random boolean (false 90% of the time)
            let deliberated = Math.random() > 0.9;

            //Random Stress level between 1 and 5 (integer)
            let stress_level = Math.floor(Math.random() * 5) + 1;

            //Random cigarettes smoked between 0 and 10 (integer)
            let cigarettes_smoked = Math.floor(Math.random() * 11);

            //Random body_parts in array [{name:"Hands"}, {name:"Ears"}, {name:"Nose"}, {name:"Feet"}] without repetition
            let body_parts = [];
            let body_parts_names = ["Hands", "Ears", "Nose", "Feet"]
            for (let i = 0; i < Math.floor(Math.random() * 3)+1; i++) {
                let index = Math.floor(Math.random() * body_parts_names.length)
                body_parts.push({name: body_parts_names[index]})
                body_parts_names.splice(index, 1)
            }

            const episode = {
                "date_time": date_time,
                "duration": duration,
                "temperature": temperature,
                "deliberated": deliberated,
                "stress_level": stress_level,
                "daily_cigarette_smoked": cigarettes_smoked,
                "body_parts": body_parts,
                "id": i,
                "user_id": user_id
            }
            
            episodes.push(episode);

        }
        return episodes;
    }

}

export default DataProcessor