import os
from fastmcp import FastMCP

mcp = FastMCP(
    name="AdditionServer",
    instructions="This server adds two numbers.",
    sse_path="/calculator/sse",
    message_path="/calculator/messages/",
)

@mcp.tool()
def competitive_analysis(a: str) -> str:
    """Given a company, return it's market position relative to its competitors"""
    #entity = top (threshold/confidence) resolve_company_entity(a)
    #determine_market(a)
    #retrieve_competitors(a)
    #for each competitor: scrape_competitor_sites(a)
    #retrieve_published_analysis(a)
    #summary_prompt
    return a

@mcp.tool()
def resolve_company_entity(a: str) -> str:
    """Given attributes such as a company name, website, or other identifiers -> attempt to determine what company it is referring to"""
    return a #json list of entities with company_name, website, aliases, match_probability, disambiguating_attribute

@mcp.tool()
def determine_market(a: float, b: float) -> float:
    """Determine the market of a company based on its attributes."""
    return a - b

@mcp.tool()
def retrieve_competitor_names(a: float, b: float) -> float:
    """Retrieve the names of competitors for a given company."""
    return a * b

@mcp.tool()
def markdown_site_crawler(a: str) -> str:
    """Given a company, scrape its website and return the text in markdown format."""
    #
    return a 

@mcp.tool()
def retrieve_published_analysis(a: float, b: float) -> float:
    """Divide two numbers and return the result."""
    return a / b

#public/private, market cap, buy/sell/hold recs, job postings count, linkedin employee count, news articles, google trends, sentiment, swot


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8001"))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
