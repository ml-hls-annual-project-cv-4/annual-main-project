from Factories.JsonDataSvcFactory import DataServiceFactory

factory = DataServiceFactory()

edaDataService = factory.GetEDADataService('../files/bdd100k_labels_images_train.json')
categories = edaDataService.GetCategories()

print('Вывод уникальных категорий:')
for category in categories:
    print(category, edaDataService.GetCategoryCount(category), sep=': ')

scenes = edaDataService.GetScenes()

print('\nВывод уникальных сцен:')
for scene in scenes:
    print(scene, edaDataService.GetSceneCount(scene), sep=': ')

weathers = edaDataService.GetWeathers()

print('\nВывод уникальных погод:')
for weather in weathers:
    print(weather, edaDataService.GetWeatherCount(weather), sep=': ')

timesOfDay = edaDataService.GetTimesOfDay()

print('\nВывод уникальных частей дня:')
for timeOfDay in timesOfDay:
    print(timeOfDay, edaDataService.GetTimeOfDayCount(timeOfDay), sep=': ')