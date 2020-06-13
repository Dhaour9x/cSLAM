import ICP

icp = ICP.ICP(
    model_image="cartographer.png",
    data_image="hector.png",
    binary_or_color="binary",
    iterations=10,
    connectivity_threshold=5,
    calculation_image_size=100,
)
icp.icp()
icp.display_results()
icp.display_results_as_movie()
