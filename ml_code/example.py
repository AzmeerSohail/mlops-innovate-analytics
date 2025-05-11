def main():
    print("🚀 Running example ML pipeline...")

    # Simulated data
    data = {
        "age": [25, 32, 47, 18],
        "salary": [50000, 60000, 80000, 30000]
    }

    # Print original data
    print("📊 Original Data:")
    for i in range(len(data['age'])):
        print(f"Age: {data['age'][i]}, Salary: {data['salary'][i]}")

    # Simple transformation (simulate salary raise)
    for i in range(len(data['salary'])):
        data['salary'][i] *= 1.1  # simulate a raise

    # Print processed data
    print("\n✅ Processed Data:")
    for i in range(len(data['age'])):
        print(f"Age: {data['age'][i]}, Salary: {data['salary'][i]:.2f}")

if __name__ == "__main__":
    main()
