import matplotlib.pyplot as plt
import seaborn as sns
import math

class Analysis:
    def __init__(self, df):
        self.df = df
         
    def plot_univariate_numerical(self,features):
        n_cols = 4
        n_rows = math.ceil(len(features) / n_cols)

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols*5, n_rows*4))
        axes = axes.flatten()

        for i, col in enumerate(features):
            sns.histplot(self.df[col].dropna(), kde=True, ax=axes[i], bins=30)
            axes[i].set_title(f'Distribution of {col}')
            
        # Turn off any unused subplots
        for j in range(i+1, len(axes)):
            axes[j].axis('off')

        plt.tight_layout()
        plt.show()

    def plot_univariate_catergorical(self,features):
        for col in features:
            if col in self.df.columns:
                plt.figure(figsize=(8, 4))
                self.df[col].value_counts(dropna=False).head(10).plot(kind='bar')
                plt.title(f'Frequency of {col}')
                plt.xlabel(col)
                plt.ylabel('Count')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

    def plot_multivariate(self):
        monthly_zip_stats = self.df.groupby(['PostalCode', 'TransactionMonth'])[['TotalPremium', 'TotalClaims']].sum().reset_index()
        plt.figure(figsize=(8, 6))
        sns.scatterplot(
            data=monthly_zip_stats,
            x='TotalPremium',
            y='TotalClaims',
            hue='PostalCode',  # Can be removed if too many zip codes
            alpha=0.7
        )
        plt.title('Total Claims vs Total Premium by Zip Code and Month')
        plt.xlabel('Total Premium')
        plt.ylabel('Total Claims')
        plt.legend(title='PostalCode', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

    def plot_corr_mat(self):
        monthly_zip_stats = self.df.groupby(['PostalCode', 'TransactionMonth'])[['TotalPremium', 'TotalClaims']].sum().reset_index()
        corr_df = monthly_zip_stats[['TotalPremium', 'TotalClaims']]
        correlation_matrix = corr_df.corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix: TotalPremium vs TotalClaims')
        plt.show()

    def plot_vehicle_premium(self):
        sns.boxplot(data=self.df, x='Gender', y='TotalClaims')
        plt.title('Claims Distribution by Gender')
        plt.show()

        sns.boxplot(data=self.df, x='VehicleType', y='TotalPremium')
        plt.xticks(rotation=45)
        plt.title('Premiums by Vehicle Type')
        plt.show()

    def plot_premium_trend(self):
        self.df['YearMonth'] = self.df['TransactionMonth'].dt.to_period('M')
        monthly_premium = self.df.groupby('YearMonth')['TotalPremium'].sum()
        monthly_premium.plot(kind='line', figsize=(10, 5), marker='o')
        plt.title('Total Premium Over Time')
        plt.ylabel('Total Premium')
        plt.xlabel('Month')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_cover_Trend(self):
        cover_type_trend = self.df.groupby(['YearMonth', 'CoverType']).size().unstack(fill_value=0)
        cover_type_trend.plot(figsize=(12, 6), marker='o')
        plt.title('Cover Type Trends Over Time')
        plt.ylabel('Number of Policies')
        plt.xlabel('Month')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_av_premium_per_cover(self):
        avg_premium_by_cover = self.df.groupby(['YearMonth', 'CoverType'])['TotalPremium'].mean().unstack()
        avg_premium_by_cover.plot(figsize=(12, 6), marker='o')
        plt.title('Average Premium per Cover Type Over Time')
        plt.ylabel('Avg Total Premium')
        plt.xlabel('Month')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_box_plots(self,cols):
        n_cols = 3
        n_rows = math.ceil(len(cols) / n_cols)

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols*5, n_rows*4))
        axes = axes.flatten()

        for i, col in enumerate(cols):
            sns.boxplot(data=self.df, x=col, ax=axes[i])
            axes[i].set_title(f'Boxplot of {col}')
            axes[i].set_xlabel('')
            
        # Turn off unused subplots
        for j in range(i + 1, len(axes)):
            axes[j].axis('off')

        plt.tight_layout()
        plt.show()








