Imagine buying a second-hand book with a screen reader. 📚

You find a book. The "add to basket" button is just an icon, so your screen reader says "button." You move on: "button." The form fields have placeholder text instead of labels, and it disappears the moment you type. The genre filter and the address autocomplete trap your keyboard focus, and you can't get out. You make a small mistake at checkout, and the only sign is red text you can't see. And none of the book covers have alt text.

One customer of Boekenbus emailed to say she couldn't complete a purchase.

Rosa Veenstra, a former librarian in Drachten, built Boekenbus in Bolt: a webshop for second-hand books, with a subscription "surprise box," search by genre and author, and a mobile-first checkout. With 14 staff across packing and customer service and turnover past €2 million, it's outside the microenterprise exemption of the European Accessibility Act.

An automated scan found 212 issues. Manual testing confirmed the customer's experience, plus pale grey text on cream that failed contrast everywhere.

What LaunchStudio changed (9 business days, €2,500):
✓ Accessible names on every button, and alt text, with book-cover alt text generated from title and author data
✓ Visible labels instead of placeholder-only fields
✓ The filter and autocomplete rebuilt on accessible patterns
✓ Text colours adjusted to meet contrast, within Rosa's palette
✓ Validation errors linked to their fields and announced
✓ Headings and landmarks, plus axe checks in CI
✓ The customer who reported the problem tested the checkout with the team before release
Rosa then published an accessibility statement.

The critical flows now meet WCAG 2.1 AA. Mobile checkout completion rose about 9% the next quarter, for all customers. And the customer who first wrote in became a regular subscriber.

"I built the shop for book lovers and forgot that some of them read with their ears. The fixes didn't change how it looks, only who can use it." - Rosa Veenstra

https://launchstudio.eu/en/blog/make-an-ai-generated-app-production-ready-for-the-european-accessibility-act

#Accessibility #EAA #WCAG #Ecommerce #LaunchStudio #Manifera
