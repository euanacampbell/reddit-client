from linkpreview import link_preview

preview = link_preview("https://www.sciencenews.org/article/sun-solar-storms-earth-havoc-space-weather-forecasts")
print("title:", preview.title)
print("description:", preview.description)
print("image:", preview.image)
print("force_title:", preview.force_title)
print("absolute_image:", preview.absolute_image)