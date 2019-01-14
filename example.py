import keywords_extractor

text = "The Valsad police on Friday arrested 18 leaders of the Khedut Samaj Gujarat for taking out a rally from Pariya village despite their permission being withdrawn. On Friday morning, over 30 farmers from the group, including KSG president Jayesh Patel, started the rally near Vapi, during which the 18 members were detained. Patel had sought permission for the rally from Navsari and Valsad collectors. While Navsari collector Ravi Kumar Arora gave permission for the rally, Valsad collector C R Kharsan denied the permission on Thursday. Subsequently, Arora also revoked the permission.While the leaders were later released, six of them restarted the rally through Valsad. Darshan Naik, a member of the Surat unit of KSG, alleged that the collectors had become victims of political parties and thus cancelled the permission."
extractor = keywords_extractor.Extractor(text)
print(extractor.rank_words())
