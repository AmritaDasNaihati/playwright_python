# import asyncio
# import pytest
# from playwright.async_api import async_playwright
# from main import page

# async def test_DiscountsTab(Code):
#         await page.locator("//p[contains(text(),'Promotions')]").click()
#         await page.locator("//p[contains(text(),'Discounts')]").click()
#         await page.get_by_role("link", name="Add new").click()
#         await page.locator("input#Name").fill("ABCD ROY")
#         await page.locator("select#DiscountTypeId").click()
#         #await page.locator("select#DiscountTypeId > option:nth-child(5)")
#         await page.locator("input#UsePercentage").check()
#         await page.locator("//input[@role='spinbutton' and @title='0.0000 ']").click()
#         await page.keyboard.press('Backspace')
#         await page.get_by_label("Discount percentage").type("20")
#         await page.locator("input#RequiresCouponCode").check()
#         await page.locator("input#CouponCode").fill(Code)
#         await page.locator("input#StartDateUtc").fill("4/10/2024"+" "+"12:00"+" "+"AM")
#         await page.locator("input#EndDateUtc").fill("4/30/2024"+" "+"7:00"+" "+"PM")
#         await page.locator("input#IsCumulative").check()
#         await page.locator("textarea#AdminComment").fill("Testing Perpose")
#         await page.get_by_role("button", name=" Save", exact=True).click()
#         result1 = await page.locator("div.alert-success").is_visible()
#         if result1 == True:
#             print("new discount has been added successfully")
        