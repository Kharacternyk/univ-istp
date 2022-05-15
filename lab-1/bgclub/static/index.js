const drawCharts = () => {
    for (const [url, id, title] of [
        ["/chart/game/language", "chart-language", "Ігри за мовами"],
        ["/chart/game/authors", "chart-authors", "Ігри за авторами"],
    ]) {
        const table = new google.visualization.DataTable();

        table.addColumn("string", "Мова");
        table.addColumn("number", "Кількість");

        fetch(url)
            .then(response => response.json())
            .then(rows => {
                const chart = new google.visualization.PieChart(
                    document.getElementById(id)
                );

                table.addRows(rows);
                chart.draw(table, {
                    title,
                    width: 350,
                    height: 200,
                });
            });
    }
};

google.charts.load("current", {"packages": ["corechart"]});
google.charts.setOnLoadCallback(drawCharts);
