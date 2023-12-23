# organik-anorganik-classification

Garbage is waste generated from products or items that have not been used for an extended period and lack functional value. The increasing volume of waste poses risks to the safety and health of waste sorters; improper waste disposal can also harm the environment. To mitigate these impacts, an automated system for categorizing images of organic and inorganic waste using CNN (Convolutional Neural Network) is required. This study optimizes the use of the CNN method by adding layers and hyperparameters to the utilized CNN architectures (InceptionV3, ResNet152, and MobileNetV3) for accurate waste classification.

This research process involves several stages, including collecting image data from the Waste Images Dataset (WID) and Waste Classification data (WCD), splitting the data into training and testing sets, performing data augmentation, tuning the model, and training the model using CNN architectures (InceptionV3, ResNet152, and MobileNetV3). Additionally, model evaluation is conducted using accuracy metrics in the Classification Report.

Test results using the WID dataset reveal that the InceptionV3 model achieves an accuracy of 0.9546, precision of 0.8906, recall of 0.8897, and F1-score of 0.8901. These findings indicate that the InceptionV3 model performs the best within the dataset, despite being tested on 9 classes. Furthermore, testing is conducted using the WCD dataset, demonstrating that the InceptionV3 model is the best-performing model in that dataset with an accuracy of 0.9351, precision of 0.9636, recall of 0.9234, and F1-score of 0.9430. These results highlight that the InceptionV3 model yields the best performance in the dataset consisting of 2 classes.

Dataset
- [dataset 1](https://github.com/garythung/trashnet) and [dataset 1](https://github.com/AgaMiko/waste-datasets-review)
- [dataset 2](https://www.kaggle.com/datasets/techsash/waste-classification-data)

This Model acctualy develop with fast API and develop with streamlit
https://wasteclassification.streamlit.app/
