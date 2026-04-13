"""
Search Routes
Handles property search and filtering endpoints
"""

from flask import Blueprint, render_template, request, jsonify
from scrapers.realestate import RealEstateAuScraper
from scrapers.domain import DomainAuScraper
from utils.filters import apply_filters

bp = Blueprint('search', __name__, url_prefix='/api/search')

@bp.route('/properties', methods=['GET'])
def search_properties():
    """
    Search for properties based on query parameters
    
    Query Parameters:
    - suburb: Property suburb
    - min_price: Minimum price
    - max_price: Maximum price
    - bedrooms: Number of bedrooms
    - bathrooms: Number of bathrooms
    - car_spaces: Number of car spaces
    - property_type: Type of property (house, unit, etc.)
    - source: Data source (realestate, domain, or both)
    """
    try:
        # Extract query parameters
        suburb = request.args.get('suburb', '').strip()
        min_price = request.args.get('min_price', type=int)
        max_price = request.args.get('max_price', type=int)
        bedrooms = request.args.get('bedrooms', type=int)
        bathrooms = request.args.get('bathrooms', type=int)
        car_spaces = request.args.get('car_spaces', type=int)
        property_type = request.args.get('property_type', '').strip()
        source = request.args.get('source', 'both').lower()
        
        if not suburb:
            return jsonify({'error': 'Suburb parameter is required'}), 400
        
        # Initialize results list
        results = []
        
        # Scrape from realestate.com.au if requested
        if source in ['realestate', 'both']:
            realestate_scraper = RealEstateAuScraper()
            realestate_results = realestate_scraper.search(suburb, property_type)
            results.extend(realestate_results)
        
        # Scrape from domain.com.au if requested
        if source in ['domain', 'both']:
            domain_scraper = DomainAuScraper()
            domain_results = domain_scraper.search(suburb, property_type)
            results.extend(domain_results)
        
        # Apply filters to results
        filtered_results = apply_filters(
            results,
            min_price=min_price,
            max_price=max_price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            car_spaces=car_spaces
        )
        
        return jsonify({
            'success': True,
            'count': len(filtered_results),
            'results': filtered_results
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/popular-suburbs', methods=['GET'])
def get_popular_suburbs():
    """Get list of popular suburbs for autocomplete"""
    popular_suburbs = [
        'Surry Hills', 'Darlinghurst', 'Bondi', 'Coogee',
        'Newtown', 'Glebe', 'Paddington', 'Redfern',
        'South Yarra', 'Fitzroy', 'Carlton', 'Brunswick',
        'Footscray', 'Moonee Ponds', 'Coburg', 'Essendon'
    ]
    return jsonify({'suburbs': popular_suburbs})

@bp.route('/filters', methods=['GET'])
def get_filter_options():
    """Get available filter options"""
    return jsonify({
        'property_types': ['House', 'Unit', 'Apartment', 'Townhouse', 'Land'],
        'sources': ['realestate', 'domain', 'both'],
        'bedrooms': [1, 2, 3, 4, 5],
        'bathrooms': [1, 2, 3, 4],
        'car_spaces': [0, 1, 2, 3, 4]
    })
