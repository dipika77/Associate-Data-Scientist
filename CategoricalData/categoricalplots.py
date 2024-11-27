#Introduction to categorical plots using seaborn

#instructions
'''Set the font size of your graphic to be 1.25.
Set the background of the graphic to be "darkgrid".
Create a boxplot using catplot() with "Helpful votes" as the continuous variable split across each "Traveler type". Make sure that you are using the reviews dataset.'''

# Set the font size to 1.25
sns.set(font_scale = 1.25)

# Set the background to "darkgrid"
sns.set_style('darkgrid')

# Create a boxplot
sns.catplot(x="Traveler type", y="Helpful votes", data=reviews, kind="box")

plt.show()



#Seaborn bar plots
#instructions
''''''
