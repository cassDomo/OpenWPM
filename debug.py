seedSitesList = open('similarweb41junefiltered.txt', 'r')
seedAddresses = seedSitesList.read().splitlines()
seedSitesList.close()
print(seedAddresses)