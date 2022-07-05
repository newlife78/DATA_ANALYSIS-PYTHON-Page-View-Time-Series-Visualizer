import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data and parse dates
df = pd.read_csv('fcc-forum-pageviews.csv', sep=',', index_col='date', parse_dates=['date'])

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(21, 7))

    ax.plot(df.index, df['value'], linestyle='-', color='#D5170E', linewidth=2)

    # Set graphic layout
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', pad=10.0, fontsize=16)
    ax.set_ylabel('Page Views', labelpad=10.0, fontsize=13.5)
    ax.set_xlabel('Date', labelpad=10.0, fontsize=13.5)
    plt.setp(ax.get_xticklabels(), fontsize=12)
    plt.setp(ax.get_yticklabels(), fontsize=12)
    ax.grid(True, color='#c0c0c0', linestyle='--')

    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['month'] = df_bar.index.month
    df_bar['year'] = df_bar.index.year
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack(level=-1, fill_value=0)

    # Rename the columns
    df_bar.columns = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Draw bar plot
    fig = df_bar.plot(figsize=(7, 6), kind='bar', legend=True, xlabel='Years', ylabel='Average Page Views').figure

    # Set graphic layout
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', pad=10.0, fontsize=12)
    plt.legend(loc='upper left', title='Months', fontsize=9)
    plt.xticks(fontsize=9, rotation=0)
    plt.yticks(fontsize=9)

    # Save image and return fig
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Sort 'df_box' by 'month'
    df_box = df_box.sort_values(by='date', key=lambda month: [d.month for d in df_box.date])

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(figsize=(20, 8), nrows=1, ncols=2)

    sns.boxplot(ax=ax1, data=df_box, x='year', y='value')
    sns.boxplot(ax=ax2, data=df_box, x='month', y='value')

    # Set 'Year-Wise Box Plot' Graphic Layout
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Set 'Month-Wise Box Plot' Graphic Layout
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
