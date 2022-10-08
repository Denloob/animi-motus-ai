try:
    import kaggle

    kaggle.api.dataset_download_files(
        "https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset",
        path="dataset",
        unzip=True,
    )
except IOError as e:
    if "Could not find kaggle.json." in str(e):
        print(
            f'{e}\nread "https://github.com/Kaggle/kaggle-api#api-credentials" to learn how to set up API credentials.'
        )
    else:
        raise e
else:
    print("Done!")
