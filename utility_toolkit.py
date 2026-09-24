from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Utility Toolkit")

@mcp.tool()
def convert_temperature(celsius: float):
    """Convert Celsius temperature to Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32

    return {
        "celsius": celsius,
        "fahrenheit": fahrenheit
    }

@mcp.tool()
def calculate_percentage(number: float, percentage: float):
    """Calculate a percentage of a given number."""
    result = (number * percentage / 100)

    return {
        "number": number,
        "percentage": percentage,
        "result": result
    }

@mcp.tool()
def calculate_uptime(total_hours: float, available_hours: float):
    """Calculate application uptime percentage."""
    if total_hours <= 0:
        return {"error": "Total hours must be greater than 0."}
    if available_hours > total_hours:
        return {"error": "Available hours cannot be greater than total hours."}
    uptime = (available_hours / total_hours )* 100
    
    return {
        "total_hours": total_hours,
        "available_hours": available_hours,
        "uptime": uptime
    }

@mcp.tool()
def check_sla_status(uptime: float, sla_target: float):
    """Check whether application uptime meets the SLA target."""
    if uptime >= sla_target:
        status = "SLA MET"
    else:
        status = "SLA BREACHED"

    return {
    "uptime": uptime,
    "sla_target": sla_target,
    "status": status
}

if __name__ == "__main__":
    mcp.run()