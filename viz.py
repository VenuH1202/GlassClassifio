import streamlit as st
#Importing Necessary Librares
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from scipy import stats
def app():
    df = pd.read_csv("glass.csv")
    st.title('Visualization')
    background_color = '#FFFED7'
    color_palette = ['#669900', '#CC99FF', '#00B050', '#00B0F0', '#FFC000', '#00FF00', '#002060', '#FF00FF', '#6600CC']
    fig = plt.figure(figsize=(12, 6))
    gs = fig.add_gridspec(1, 2)
    gs.update(wspace=0.3, hspace=0.25)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])

    fig.patch.set_facecolor(background_color)
    ax0.set_facecolor(background_color)
    ax1.set_facecolor(background_color)

    # Title
    ax0.text(0.5, 0.5, 'Countplot of the Type\n _______________',
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=18, fontfamily='serif', fontweight='bold')
    ax0.set_xticklabels([])
    ax0.set_yticklabels([])
    ax0.tick_params(left=False, bottom=False)
    ax0.spines['bottom'].set_visible(False)

    # Type
    ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    sns.countplot(x='Type', data=df, palette=color_palette, ax=ax1)
    ax1.set_xlabel('')
    ax1.set_ylabel('')

    axes = [ax0, ax1]
    for s in ["top", "right", "left"]:
        for ax in axes:
            ax.spines[s].set_visible(False)
    st.pyplot(fig)
    fig = plt.figure(figsize=(18, 15))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.5, hspace=0.25)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])
    ax2 = fig.add_subplot(gs[0, 2])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    ax5 = fig.add_subplot(gs[1, 2])
    ax6 = fig.add_subplot(gs[2, 0])
    ax7 = fig.add_subplot(gs[2, 1])
    ax8 = fig.add_subplot(gs[2, 2])

    axes = [ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
    fig.patch.set_facecolor(background_color)

    # Title
    ax1.text(0, 19, 'Boxenplot for continuous features',
             fontsize=18, fontfamily='serif', fontweight='bold',
             horizontalalignment='center',
             verticalalignment='center')

    for i, ax in enumerate(axes):
        ax.set_facecolor(background_color)
        ax.set_title(df.columns[i], fontsize=14, fontfamily='serif', fontweight='bold')
        ax.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))

        sns.boxenplot(y=df.columns[i], data=df, ax=ax, palette=[color_palette[i]], width=0.6)
        ax.set_xlabel('')
        ax.set_ylabel('')

        for s in ["top", "right", "left"]:
            ax.spines[s].set_visible(False)
    st.pyplot(fig)
    fig = plt.figure(figsize=(18, 15))
    gs = fig.add_gridspec(3, 3)
    gs.update(wspace=0.3, hspace=0.4)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])
    ax2 = fig.add_subplot(gs[0, 2])
    ax3 = fig.add_subplot(gs[1, 0])
    ax4 = fig.add_subplot(gs[1, 1])
    ax5 = fig.add_subplot(gs[1, 2])
    ax6 = fig.add_subplot(gs[2, 0])
    ax7 = fig.add_subplot(gs[2, 1])
    ax8 = fig.add_subplot(gs[2, 2])

    axes = [ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
    kde_palette = color_palette[0:6]
    fig.patch.set_facecolor(background_color)

    # Title
    ax1.text(14.5, 0.35, 'Distribution for continuous features by Type',
             fontsize=18, fontfamily='serif', fontweight='bold',
             horizontalalignment='center',
             verticalalignment='center')

    for i, ax in enumerate(axes):
        dp_legend = False
        if i in [2, 5, 8]:
            dp_legend = True

        ax.set_facecolor(background_color)
        ax.set_title(df.columns[i], fontsize=14, fontfamily='serif', fontweight='bold')
        ax.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))

        sns.kdeplot(x=df.columns[i], hue='Type', data=df, fill=True, ax=ax, palette=kde_palette, legend=dp_legend)
        ax.set_xlabel('')
        ax.set_ylabel('')

        for s in ["top", "right", "left"]:
            ax.spines[s].set_visible(False)
    st.pyplot(fig)
    df_cor = df.drop('Type', axis=1).corr()
    fig = plt.figure(figsize=(10, 10))
    gs = fig.add_gridspec(1, 1)
    gs.update(wspace=0.3, hspace=0.1)
    ax0 = fig.add_subplot(gs[0, 0])

    mask = np.triu(np.ones_like(df_cor))
    ax0.text(2.5, -0.1, 'Correlation Matrix', fontsize=18, fontweight='bold',
             fontfamily='serif')
    sns.heatmap(df_cor, annot=True, fmt='.2f', cmap='RdBu', square=True, mask=mask, linewidth=0.7)
    st.pyplot(fig)
    fig = plt.figure(figsize=(12, 15))
    gs = fig.add_gridspec(5, 2)
    gs.update(wspace=0.3, hspace=0.3)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])
    ax2 = fig.add_subplot(gs[1, 0])
    ax3 = fig.add_subplot(gs[1, 1])
    ax4 = fig.add_subplot(gs[2, 0])
    ax5 = fig.add_subplot(gs[2, 1])
    ax6 = fig.add_subplot(gs[3, 0])
    ax7 = fig.add_subplot(gs[3, 1])
    ax8 = fig.add_subplot(gs[4, 0])
    ax9 = fig.add_subplot(gs[4, 1])

    axes = [ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]
    fig.patch.set_facecolor(background_color)

    # Ca and RI
    cor = round(stats.pearsonr(df['Ca'], df['RI'])[0], 4)
    ax0.text(0.5, 0.5,
             'Scatter plot for\n Ca and RI\n _________________',
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=18, fontfamily='serif',
             fontweight='bold')
    ax0.text(0.5, 0.15,
             'cor = ' + str(cor),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=14, fontfamily='serif',
             fontweight='bold')

    ax1.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    sns.scatterplot(x='Ca', y='RI', data=df, ax=ax1, color=color_palette[0])

    # Si and RI
    cor = round(stats.pearsonr(df['Si'], df['RI'])[0], 4)
    ax2.text(0.5, 0.5,
             'Scatter plot for\n Si and RI\n _________________',
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=18, fontfamily='serif',
             fontweight='bold')
    ax2.text(0.5, 0.15,
             'cor = ' + str(cor),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=14, fontfamily='serif',
             fontweight='bold')

    ax3.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    sns.scatterplot(x='Si', y='RI', data=df, ax=ax3, color=color_palette[1])

    # Ba and Mg
    cor = round(stats.pearsonr(df['Ba'], df['Mg'])[0], 4)
    ax4.text(0.5, 0.5,
             'Scatter plot for\n Ba and Mg\n _________________',
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=18, fontfamily='serif',
             fontweight='bold')
    ax4.text(0.5, 0.15,
             'cor = ' + str(cor),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=14, fontfamily='serif',
             fontweight='bold')

    ax5.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    sns.scatterplot(x='Ba', y='Mg', data=df, ax=ax5, color=color_palette[2])

    # Ba and Al
    cor = round(stats.pearsonr(df['Ba'], df['Al'])[0], 4)
    ax6.text(0.5, 0.5,
             'Scatter plot for\n Ba and Al\n _________________',
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=18, fontfamily='serif',
             fontweight='bold')
    ax6.text(0.5, 0.15,
             'cor = ' + str(cor),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=14, fontfamily='serif',
             fontweight='bold')

    ax7.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    sns.scatterplot(x='Ba', y='Al', data=df, ax=ax7, color=color_palette[3])

    # Al and Mg
    cor = round(stats.pearsonr(df['Al'], df['Mg'])[0], 4)
    ax8.text(0.5, 0.5,
             'Scatter plot for\n Al and Mg\n _________________',
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=18, fontfamily='serif',
             fontweight='bold')
    ax8.text(0.5, 0.15,
             'cor = ' + str(cor),
             horizontalalignment='center',
             verticalalignment='center',
             fontsize=14, fontfamily='serif',
             fontweight='bold')

    ax9.grid(color='#000000', linestyle=':', axis='y', zorder=0, dashes=(1, 5))
    sns.scatterplot(x='Al', y='Mg', data=df, ax=ax9, color=color_palette[4])

    for ax in axes:
        ax.set_facecolor(background_color)
        ax.set_xlabel('')
        ax.set_ylabel('')
        for s in ['top', 'right']:
            ax.spines[s].set_visible(False)

    for ax in [ax0, ax2, ax4, ax6, ax8]:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.tick_params(left=False, bottom=False)
        for s in ['left', 'bottom']:
            ax.spines[s].set_visible(False)
    st.pyplot(fig)
    
