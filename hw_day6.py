# You are building a basic dashboard for a blog website. The blog has a list that stores the number of views for different blog posts.
# Your task is to:
# Loop through the given list of blog post views.
# For each blog post:
# If views > 1000, print "Trending"
# If views between 500 and 1000, print "Average"
# If views < 500, print "Low Traffic"
# After the loop:
# Print the total number of views
# Print how many posts were "Trending"
# Use this list for blog views:
# blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

blog_views=[150,800,2500,600,1200,450,3000]
trend=0
avg=0
low=0
total_views=0
for views in blog_views:
    if views>1000:
        print("Trending")
        trend=trend+1
    elif 500 < views < 1000:
        print("Average")
        avg=avg+1
    else :
        print("Low Traffic")
        low=low+1
total_views=trend+avg+low
print("The total no.of views:",total_views)
print("No.of posts that is trending is:",trend)


