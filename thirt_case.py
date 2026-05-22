
# Escolhi criar esse gráfico por curiosidade pessoal. 
# Queria descobrir quais foram os filmes mais votados do IMDB em um ano específico
# e achei interessante representar, ao mesmo tempo, a quantidade de votos e a nota
# de cada filme de forma visual e comparativa.

# O ano escolhido foi 2016, principalmente por conta do interesse pessoal no filme do deadpool.

# Utilizei o ChatGPT para me ajudar na estética do gráfico, como tamanho de letras, cores e disposição dos elementos.

import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://looqbox-challenge:looq-challenge@35.199.115.174:3306/looqbox-challenge"
)

def plot_chart(ano_requisitado):

    query = """
        SELECT 
            Title,
            Year,
            Rating,
            Votes
        FROM IMDB_movies
        WHERE Year = %s
        ORDER BY Votes DESC
        LIMIT 5
    """

    df = pd.read_sql(
        query,
        engine,
        params=(ano_requisitado,)
    )

    fig, ax = plt.subplots(figsize=(16, 8))

    bars = ax.bar(
        df['Title'],
        df['Votes'],
        edgecolor='black',
        linewidth=1.5
    )

    for bar, rating in zip(bars, df['Rating']):

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() / 2,
            f'Rating\n{rating}',
            ha='center',
            va='center',
            fontsize=12,
            fontweight='bold',
            color='white'
        )

    for bar, votes in zip(bars, df['Votes']):

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + (height * 0.02),
            f'{votes:,} votes',
            ha='center',
            va='bottom',
            fontsize=11,
            fontweight='bold'
        )

    ax.set_title(
        f'Top 5 Most Voted IMDB Movies - {ano_requisitado}',
        fontsize=20,
        fontweight='bold',
        pad=20
    )

    ax.set_xlabel(
        'Movies',
        fontsize=14,
        fontweight='bold'
    )

    ax.set_ylabel(
        'Votes',
        fontsize=14,
        fontweight='bold'
    )

    ax.grid(
        axis='y',
        linestyle='--',
        alpha=0.2
    )

    plt.yticks(fontsize=11)

    plt.tight_layout()

    plt.show()


plot_chart(2016)