"""Example usage of swagou as a library."""

import os
import sys

# Add the parent directory to the path so we can import swagou
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from swagou.filter import filter_openapi_schema


def main():
    """Run an example filtering operation."""
    # Replace with an actual OpenAPI schema file or URL
    input_source = "example_schema.yaml"

    # Example filtering parameters
    get_paths = ["/api/posts/", "/api/posts/{slug}/"]
    all_paths = ["/api/users/*"]

    try:
        # Filter the schema
        filtered_schema = filter_openapi_schema(
            input_source=input_source,
            get_paths=get_paths,
            all_paths=all_paths,
        )

        # Print the filtered schema
        print(filtered_schema)

        # Optionally save to a file
        with open("filtered_schema.yaml", "w", encoding="utf-8") as f:
            f.write(filtered_schema)

        print(f"Filtered schema saved to filtered_schema.yaml")

    except Exception as e:
        print(f"Error: {str(e)}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
