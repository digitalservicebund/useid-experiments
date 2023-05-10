# Check which identification apps are installed
Users might have either AusweisApp2 or Bundesident installed. We want to guide them correctly to the installed app or communicate to them what to do, when they do not have the app installed. For this it would be good to check, what app is installed.

You can find here the experimentation together with a prototype and the results here.

## Results
We can only direct the user into the apps if they are installed or show a different webpage through a timeout in case the user does not have one or both apps installed. However, it is not possible to silently detect in the background which app is installed and then guide the user according to this.
The way it works is basically that we set a timeout before we redirect the user into the app. When the timeout is hit we will redirect the browser to our fallback page. If the user could open the link in the app (has it installed), the timeout could be intercepted and we could show some different message instead. 
**Note:** This does use timeouts and could potentially be a) not very accessible and b) has a lot of potential edge cases.

For Android and iOS we had the following results for different experiments


Experiment | Android | iOS
---|---|---
Special scheme is used to open app (bundesident://...) | Works | Works with pop ups
Universal Link is used | Works | Works without popups
Link is set through embedded ifram | Works | Does not work


This does look quite smooth in Android. However, the user would see a pop-up screen for a short second before being redirect if any app is not installed.