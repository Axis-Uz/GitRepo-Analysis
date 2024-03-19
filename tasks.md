Link To Dataset - [Kaggle Dataset](https://www.kaggle.com/datasets/donbarbos/github-repos)

- [ ] Data Cleaning: Remove Outlier and Some More Columns
- [ ] Clustering
  - [ ] Cluster the data around the usage of popular languages
- [ ] Feature Extraction
  - [x] Whether or not the reposiotory have webpage - `Homepage`
  - [x] How recent the update time was -- `UpdateDate`-`Today`
  - [x] Extract the lenght of words used in description, name and such.
  - [x] Convert the Size Scale, which is in bytes -- $x\times 10^6$
      - [ ] Forget to add into the Data Cleaning 
  - [ ] Predict whether the repo is popular or not
    - [x] Create a new feature that asssigns the popularity on the basis [Popular Conditions](data/popular_repo.md)
    - [ ] Models That Can Be Used
      - [ ] Logistic Regression
      - [ ] KNN
      - [ ] Random Forest