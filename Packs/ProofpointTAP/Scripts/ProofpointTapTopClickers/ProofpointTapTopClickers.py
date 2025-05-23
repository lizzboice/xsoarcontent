import demistomock as demisto  # noqa: F401
from CommonServerPython import *  # noqa: F401


def main():
    try:
        results: dict = demisto.executeCommand("proofpoint-get-top-clickers", {"window": 90})[0]  # type: ignore
        contents = results.get("Contents")

        users = []
        if isinstance(contents, dict):
            # In the case the command is not available, this value will return as str.
            # Unsupported Command..
            users = contents.get("users", [])

        users_res_for_chart = []
        for user in users:
            users_res_for_chart.append(
                {"name": user.get("identity").get("emails", [""])[0], "data": [user.get("clickStatistics").get("clickCount")]}
            )
        default_empty_chart_data = [
            {"name": "", "data": [], "color": ""},
        ]

        final_res = users_res_for_chart if users_res_for_chart else default_empty_chart_data
        return_results(json.dumps(final_res))

    except Exception as e:
        raise DemistoException(f"Script failed with the following error: {e}")


if __name__ in ["__main__", "builtin", "builtins"]:
    main()
