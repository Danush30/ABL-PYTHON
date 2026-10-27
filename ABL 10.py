def manufacturing_quality_control():
    products = ["Product A", "Product B", "Product C"]

    # Each row represents a product; each value is [produced, defective].
    batches = [
        [[100, 3], [120, 8], [150, 5]],
        [[200, 12], [180, 6], [160, 4]],
        [[90, 2], [110, 10], [130, 3]]
    ]

    quality_threshold = 5

    for i, product in enumerate(products):
        print(f"\n{product}")
        total_produced = 0
        total_defective = 0

        for j, (produced, defective) in enumerate(batches[i], 1):
            defect_percentage = defective / produced * 100

            total_produced += produced
            total_defective += defective

            print(f"\nBatch {j}")
            print("Units produced:", produced)
            print("Defective units:", defective)
            print(f"Defect percentage: {defect_percentage:.2f}%")

            if defect_percentage > quality_threshold:
                print("Quality status: EXCEEDS THRESHOLD")
            else:
                print("Quality status: ACCEPTABLE")

        overall_rate = total_defective / total_produced * 100

        print(f"\nTotal produced: {total_produced}")
        print(f"Total defective: {total_defective}")
        print(f"Overall defect rate: {overall_rate:.2f}%")

    print("\nQuality control analysis completed.")


if __name__ == "__main__":
    manufacturing_quality_control()