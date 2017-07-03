# Sublime text 3 plugin for Vtex tags
# Copyright Rodrigo Navarro 2017
# MIT LICENSE

import sublime
import sublime_plugin
import json
import os


class VtexCommand(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		current_file = view.file_name()
		if current_file is None:
			return None;

		completions = []
		file_name, file_extension = os.path.splitext(current_file)
		html_extensions = [
			'.html',
			'.hbs',
			'.jsx'
		]

		if file_extension in html_extensions:
			return (self.getCompletions())
		else:
			return None

	def getCompletions(self):
		completionList = [
	        { "trigger": "<vtex_html", "contents": "<!DOCTYPE html>\n<html xmlns='http://www.w3.org/1999/xhtml' xmlns:vtex='http://www.vtex.com.br/2009/vtex-common' xmlns:vtex.cmc='http://www.vtex.com.br/2009/vtex-commerce' lang='en-us'>\n<head></head>\n<body></body>\n</html>" },
	        { "trigger": "<vtex_tamplate", "contents": "<vtex:template id=\"\" />" },
	        { "trigger": "<vtex_breadcrumb", "contents": "<vtex.cmc:breadCrumb />" },
	        { "trigger": "<vtex_searchBox", "contents": "<vtex.cmc:fullTextSearchBox/>" },
	        { "trigger": "<vtex_navigationHistory", "contents": "<vtex.cmc:navigationHistory/>" },
	        { "trigger": "<vtex_storeFlagLocator", "contents": "<vtex.cmc:storeFlagLocator/>" },
	        { "trigger": "<vtex_welcomeMessage", "contents": "<vtex.cmc:welcomeMessage/>" },
	        { "trigger": "<vtex_metaTags", "contents": "<vtex:metaTags/>" },
	        { "trigger": "<vtex_departmentLinks", "contents": "<vtex.cmc:departmentLinks/>" },
	        { "trigger": "<vtex_department_navigator", "contents": "<vtex.cmc:departmentNavigator/>" },
	        { "trigger": "<vtex_pageTitle", "contents": "<vtex.cmc:searchTitle />" },
	        { "trigger": "<vtex_quickView", "contents": "<vtex.cmc:productQuickView/>" },
	        { "trigger": "<vtex_productList", "contents": "<vtex.cmc:ProductQueryStringReferenceShelf layout={0} temCount={1} columnCount={2}/>" },
	        { "trigger": "<vtex_productGifts\t Product", "contents": "<vtex.cmc:ProductGifts />" },
	        { "trigger": "<vtex_productTitle\t Product", "contents": "<vtex.cmc:productPageTitle />" },
	        { "trigger": "<vtex_productName\t Product", "contents": "<vtex.cmc:productName/>" },
	        { "trigger": "<vtex_productBrand\t Product", "contents": "<vtex.cmc:brandName/>" },
	        { "trigger": "<vtex_productMainImage\t Product", "contents": "<vtex.cmc:ProductImage/>" },
	        { "trigger": "<vtex_productCodReference\t Product", "contents": "<vtex.cmc:productReference/>" },
	        { "trigger": "<vtex_productHistoryPrices\t Product", "contents": "<vtex.cmc:StockKeepingUnitPriceHistory Months={0} Percentile={1}/>" },
	        { "trigger": "<vtex_productSku\t Product", "contents": "<vtex.cmc:skuReference/>" },
	        { "trigger": "<vtex_productPrice\t Product", "contents": "<vtex.cmc:skuPrice/>" },
	        { "trigger": "<vtex_productSkuRichSelection\t Product", "contents": "<vtex.cmc:skuRichSelection changeImage={0} />" },
	        { "trigger": "<vtex_productSkuSelection\t Product", "contents": "<vtex.cmc:skuSelection />" },
	        { "trigger": "<vtex_productOtherPayments\t Product", "contents": "<vtex.cmc:OtherPaymentMethod/>" },
	        { "trigger": "<vtex_productDelivery\t Product", "contents": "<vtex.cmc:Delivery/>" },
	        { "trigger": "<vtex_productShipingValue\t Product", "contents": "<vtex.cmc:shippingValue/>" },
	        { "trigger": "<vtex_productStockKeepingUnitRewardValue\t Product", "contents": "<vtex.cmc:stockKeepingUnitRewardValue/>" },
	        { "trigger": "<vtex_productStockKeepingUnitService\t Product", "contents": "<vtex.cmc:stockKeepingUnitService/>" },
	        { "trigger": "<vtex_productBuyTogether\t Product", "contents": "<vtex.cmc:BuyTogether/>" },
	        { "trigger": "<vtex_productDescription\t Product", "contents": "<vtex.cmc:ProductDescription/>" },
	        { "trigger": "<vtex_productShortDescription\t Product", "contents": "<vtex.cmc:productDescriptionShort />" },
	        { "trigger": "<vtex_productSpecification\t Product", "contents": "<vtex.cmc:productSpecification/>" },
	        { "trigger": "<vtex_productDimensions\t Product", "contents": "<vtex.cmc:stockKeepingUnitMeasures/>" },
	        { "trigger": "<vtex_productTags\t Product", "contents": "<vtex.cmc:ProductTag/>" },
	        { "trigger": "<vtex_productSearchInside\t Product", "contents": "<vtex.cmc:PageSearch/>" },
	        { "trigger": "<vtex_productBuyButton\t Product", "contents": "<vtex.cmc:BuyButton/>" },
	        { "trigger": "<vtex_productAsyncBuyButton\t Product", "contents": "<vtex.cmc:BuyInPage/>" },
	        { "trigger": "<vtex_productAmountAndUnitSelection\t Product", "contents": "<vtex.cmc:stockKeepingUnitAmountAndUnitSelection />" },
	        { "trigger": "<vtex_productEvaluationRate\t Product", "contents": "<vtex.cmc:evaluationRate/>" },
	        { "trigger": "<vtex_productReviews\t Product", "contents": "<vtex.cmc:UserReview/>" },
	        { "trigger": "<vtex_productAddToList\t Product", "contents": "<vtex.cmc:giftListInsertSku/>" },
	        { "trigger": "<vtex_productAddToGiftList\t Product", "contents": "<vtex.cmc:GiftListFormV2/>" },
	        { "trigger": "<vtex_productHighlight\t Product", "contents": "<vtex.cmc:HightLight/>" },
	        { "trigger": "<vtex_productDiscountHighlight\t Product", "contents": "<vtex.cmc:discountHightLight/>" },
	        { "trigger": "<vtex_productSellerOptions\t Product", "contents": "<vtex.cmc:SellerOptions />" },
	        { "trigger": "<vtex_productSellerDescription\t Product", "contents": "<vtex.cmc:sellerDescription />" },
	        { "trigger": "<vtex_productSellerInfo\t Product", "contents": "<vtex.cmc:sellerInfo />" },
	        { "trigger": "<vtex_productSalesChannelDroplist\t Product", "contents": "<vtex.cmc:SalesChannelDropList />" },
	        { "trigger": "<vtex_productFacebookLikes\t Product", "contents": "<vtex.cmc:facebookLike />" },
	        { "trigger": "<vtex_productRichSnnipetsGoogle\t Product", "contents": "<vtex.cmc:productRichSnippets showGoogle={0} />" },
	        { "trigger": "<vtex_productRichSnnipetsFacebook\t Product", "contents": "<vtex.cmc:productRichSnippets showFacebook={0} fbAdmins={1} fbAppId={2} />" },
	        { "trigger": "<vtex_productRichSnnipetsTwitter\t Product", "contents": "Twitter={0}" },
	        { "trigger": "<vtex_contentPlaceholder", "contents": "<vtex:contentPlaceHolder id={0} />" },
	        { "trigger": "<vtex_advanceSearchFilter\t Department-Category", "contents": "<vtex.cmc:advancedSearchFilter/>" },
	        { "trigger": "<vtex_singleDepartmentNavigator\t Department-Category", "contents": "<vtex.cmc:singleDepartmentNavigator/>" },
	        { "trigger": "<vtex_searchNavigator\t Department-Category", "contents": "<vtex.cmc:searchNavigator/>" },
	        { "trigger": "<vtex_searchResult\t Department-Category", "contents": "<vtex.cmc:searchResult layout={0} itemCount={1} columnsCount={2} />" },
	        { "trigger": "<vtex_miniCart\t Department-Category", "contents": "<vtex.cmc:miniCart/>" },
	        { "trigger": "<vtex_amountItemsInCart\t Department-Category", "contents": "<vtex.cmc:AmountItemsInCart/>" }
	    ]

		completions = []

		for current in completionList:
			tmp = [current["trigger"], current["contents"]]
			completions.append(tmp)

		completions.sort()
		return completions