# AIML_project_dataset

The first type of dataset is generated starting from the *cartoon* domain of *PACS* database and some categories of the *clipart* domain of *DomainNet* database, the second and the third only from *cartoon*, the fourth is the result of the union of all *PACS* domains and for the last one the *clipart* categories are used.<br>
The *scripts* folder contains the python scripts used for the generation of the datasets whereas in the *csv_files* there is the list of all the semantic quaterne created for the fifth dataset.

* **dataset_1**<br><img src="./img/dataset_1.PNG" width="300" height="300" align='left'/>
	Each set contains three identical images and the same image with different colors.
<br><br><br><br><br><br><br><br><br><br><br><br><br>
    
* **dataset_2**<br><img src="./img/dataset_2.PNG" width="300" height="300" align='left'/>
	Each set contains three different images belonging to the same class and one image from a different class.
<br><br><br><br><br><br><br><br><br><br><br><br><br>

* **dataset_3**<br><img src="./img/dataset_3.PNG" width="300" height="300" align='left'/>
	Like dataset_2, but the RGB channels of the four images are randomly reversed.
<br><br><br><br><br><br><br><br><br><br><br><br><br>

* **dataset_4**<br><img src="./img/dataset_4.PNG" width="300" height="300" align='left'/>
	Each set contains three different images belonging to the same class but different domain and one image from different class and random domain.
<br><br><br><br><br><br><br><br><br><br><br><br><br>
     
* **dataset_5**<br><img src="./img/dataset_5.PNG" width="300" height="300" align='left'/>
	Each set contains three completely different but semantically related images and an odd.
