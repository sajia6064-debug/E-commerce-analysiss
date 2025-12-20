import matplotlib.pyplot as plt
sum_amount = 438000  
plt.figure(figsize=(4,2))
plt.text(0.5, 0.6, f"{sum_amount/1000:.0f}K", ha='center', fontsize=30, color="black")
plt.text(0.5, 0.2, "Sum of Amount", ha='center', fontsize=12, color="black")
plt.axis("off")
plt.gca().set_facecolor("#1A2B8F") 
plt.show()
