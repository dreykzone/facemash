
const imagesVote = document.querySelectorAll("[data-vote]");
const loading = document.getElementById("loading");
const ctx = document.getElementById('ranking');

if (imagesVote.length) {
    async function loadPersons() {
        try {
            const response = await fetch("/api/v0/persons", {
                method: 'GET'
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Something went wrong:', error);
        }
    }

    async function renderPersons() {
        const persons = await loadPersons();
        imagesVote.forEach((element, index) => {
            element.style.backgroundImage = `url('${persons[index].image_url}')`;
            element.setAttribute("data-person", persons[index].id)
        })
    }

    renderPersons()

    async function voteRating(dataVote) {
        try {
            ativarLoading()
            const response = await fetch('/api/v0/persons', {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(dataVote)
            });

            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            return data;

        } catch (error) {
            console.error('There was an error:', error);
        } finally {
            desativarLoading()
        }
    }

    function voteImage(e) {
        let id_winner = Number(this.dataset.person);
        let id_loser = 0

        imagesVote.forEach((element) => {
            if (element !== this) {
                id_loser = Number(element.dataset.person);
            }
        })

        const data = {
            id_winner: id_winner,
            id_loser: id_loser,
        };

        voteRating(data)
        renderPersons()

    }

    imagesVote.forEach((element) => {
        element.addEventListener("click", voteImage)
    })
}

if (loading) {
    function ativarLoading() {
        loading.classList.add("active");
    }

    function desativarLoading() {
        loading.classList.remove("active");
    }
}

if (ctx) {

    async function loadRanking() {
        try {
            const response = await fetch("/api/v0/ranking", {
                method: 'GET'
            });
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Something went wrong:', error);
        }
    }

    async function renderRanking() {
        let ranking = await loadRanking();
        ranking.push(1, 2, 3, 4, 5);
        if (ranking.length >= 3) {
            ranking = ranking.filter((item, index) => index < 3)
        }
        let names = ranking.map((item) => item.name);
        let rating = ranking.map((item) => item.rating);
        console.log(ranking)
        console.log(names, rating)
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: names,
                datasets: [{
                    label: '# of Votes',
                    data: rating,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)'
                    ],
                    borderColor: [
                        'rgb(255, 99, 132)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 6000
                    }
                }
            }
        });
    }

    renderRanking()
}