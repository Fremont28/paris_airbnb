#import dataset 
paris=pd.read_csv("paris.csv",encoding='latin-1')
paris.head() 

import matplotlib.pyplot as plt 
pd.options.display.mpl_style='default'

#count property types
paris["property_type"].value_counts() 
paris.groupby('property_type').count() 
#subset properties 
paris_prop=paris[(paris.property_type=="Apartment") | (paris.property_type=="Loft")|(paris.property_type=="Bed & Breakfast")]
paris_prop["property_type"].value_counts() 
#visualize 
paris_prop['price'].hist(by=paris_prop['property_type'])
plt.show() 

#reviews per month vs. cancellation policy (no big incentive)
paris['reviews_per_month'].hist(by=paris['cancellation_policy'])
plt.show() 

#square feet vs price? 
plt.scatter(paris.square_feet,paris.price)
plt.title('Money Will Only Buy You So Much Square Feet in  Paris')
plt.xlabel('X')
plt.ylabel('Y')
plt.show() 

#correlation price vs. square feet
paris['price'].corr(paris['square_feet']) #0.29 

#boxplot (review scores rating)
sns.boxplot([paris.review_scores_rating])
plt.title('Paris Airbnb Users Are Positive Reviewers')
plt.xlabel('Review Score Rating')
plt.show() 

#service fees (i.e. cleaning fees?)
paris['clean_fee_percent']=paris['cleaning_fee']/paris['weekly_price']
sns.boxplot([paris.clean_fee_percent])
plt.title
plt.xlabel('Cleaning fee as a percent of weekly price')
plt.show() 

#occupancy rates? (available 30 days) compared to hotels?
paris['occ_30_avg']=30- paris['availability_30']
sns.distplot([paris.occ_30_avg])
plt.title
plt.xlabel('Airbnb Occupancy 30 Days')
plt.show() 

# last review minus first review(roughly how long are renters with Airbnb?)
paris['rent_length']=paris['last_review']-paris['first_review']
sns.boxplot([paris.rent_length])
plt.title
plt.xlabel('rent length (days)')
plt.show() 

#is it cheaper to rent for a week or a month?
paris_weekly=paris['weekly_price']
paris_weekly.describe() 
paris_monthly=paris['monthly_price']
paris_monthly.describe()

#bed_type vs. weekly price
paris["bed_type"].value_counts() #real bed 89.6% 

#weekly price vs. cleaning fee
paris['total_week_price']=paris['weekly_price']+paris['cleaning_fee']
clean_fee_percent=paris['cleaning_fee']/paris['total_week_price']
clean_fee_percent.mean() #5.7% of total cost

#minimum nights?
paris['length_rentals']=paris['last_review']-paris['first_review']

##offering wireless?
wireless_apt=paris[paris['amenities'].str.contains("Wireless Internet",na=False)]
wireless_apt.shape #93.9% wireless internet

#reviews/day-rough estimate length_rentals 
paris['reviews_day']=paris['number_of_reviews']/paris['length_rentals']
paris=paris[np.isfinite(paris['reviews_day'])] #remove nan 
paris['reviews_day'].describe() 

#how flex is your schedule 30 vs. 60 day availability?
paris['diff_60_30_day']=paris['availability_60']-paris['availability_30']
paris['diff_60_30_day'].mean() #10.4 days available 60 vs. 30 days

#instant bookable?
paris["instant_bookable"].value_counts()
paris['review_scores_rating'].mean() 































































