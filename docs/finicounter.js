async function getViews() {
    let url = "https://finicounter.eu.org/counter?host=" + window.location.hostname;
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function renderViews() {
    let res = await getViews();
    let elem = document.getElementById("finicount_views");
    if (typeof elem !== 'undefined' && elem !== null) {
        elem.innerText = formatNumber(res.views);
    }
}

function formatNumber(num) {
    return num.toString().replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
}

renderViews();
