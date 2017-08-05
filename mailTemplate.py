html_body=u'''<!DOCTYPE html>
<html>
<head>
	<!-- NAME: 1 COLUMN -->
	<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
	<meta content="width=device-width, initial-scale=1.0" name="viewport">
	<title>Gtrans News Letter</title>
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
	<style type="text/css">
	       body,#bodyTable,#bodyCell{
	           height:100%%%% !important;
	           margin:0;
	           padding:0;
	           width:100%%%% !important;
	       }
	       table{
	           border-collapse:collapse;
	       }
	       img,a img{
	           border:0;
	           outline:none;
	           text-decoration:none;
	       }
	       h1,h2,h3,h4,h5,h6{
	           margin:0;
	           padding:0;
	       }
	       p{
	           margin:1em 0;
	           padding:0;
	       }
	       a{
	           word-wrap:break-word;
	       }
	       .ReadMsgBody{
	           width:100%%%%;
	       }
	       .ExternalClass{
	           width:100%%%%;
	       }
	       .ExternalClass,.ExternalClass p,.ExternalClass span,.ExternalClass font,.ExternalClass td,.ExternalClass div{
	           line-height:100%%%%;
	       }
	       table,td{
	           mso-table-lspace:0pt;
	           mso-table-rspace:0pt;
	       }
	       #outlook a{
	           padding:0;
	       }
	       img{
	           -ms-interpolation-mode:bicubic;
	       }
	       body,table,td,p,a,li,blockquote{
	           -ms-text-size-adjust:100%%%%;
	           -webkit-text-size-adjust:100%%%%;
	       }
	       #bodyCell{
	           padding:20px;
	       }
	       .Image{
	           vertical-align:bottom;
	       }
	       .TextContent img{
	           height:auto !important;
	       }
	   /*
	   @tab Page
	   @section background style
	   @tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.
	   */
	       body,#bodyTable{
	           /*@editable*/background-color:#ffffff;
	       }
	   /*
	   @tab Page
	   @section background style
	   @tip Set the background color and top border for your email. You may want to choose colors that match your company's branding.
	   */
	       #bodyCell{
	           /*@editable*/border-top:0;
	       }
	   /*
	   @tab Page
	   @section email border
	   @tip Set the border for your email.
	   */
	       #templateContainer{
	           /*@editable*/border:0;
	       }
	   /*
	   @tab Page
	   @section heading 1
	   @tip Set the styling for all first-level headings in your emails. These should be the largest of your headings.
	   @style heading 1
	   */
	       h1{
	           /*@editable*/color:#606060 !important;
	           display:block;
	           /*@editable*/font-family:'Roboto',Helvetica;
	           /*@editable*/font-size:40px;
	           /*@editable*/font-style:normal;
	           /*@editable*/font-weight:bold;
	           /*@editable*/line-height:125%%%%;
	           /*@editable*/letter-spacing:-1px;
	           margin:0;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Page
	   @section heading 2
	   @tip Set the styling for all second-level headings in your emails.
	   @style heading 2
	   */
	       h2{
	           /*@editable*/color:#404040 !important;
	           display:block;
	           /*@editable*/font-family: 'Roboto',Helvetica;
	           /*@editable*/font-size:26px;
	           /*@editable*/font-style:normal;
	           /*@editable*/font-weight:bold;
	           /*@editable*/line-height:125%%%%;
	           /*@editable*/letter-spacing:-.75px;
	           margin:0;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Page
	   @section heading 3
	   @tip Set the styling for all third-level headings in your emails.
	   @style heading 3
	   */
	       h3{
	           /*@editable*/color:#606060 !important;
	           display:block;
	           /*@editable*/font-family:'Roboto',Helvetica;
	           /*@editable*/font-size:18px;
	           /*@editable*/font-style:normal;
	           /*@editable*/font-weight:bold;
	           /*@editable*/line-height:125%%%%;
	           /*@editable*/letter-spacing:-.5px;
	           margin:0;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Page
	   @section heading 4
	   @tip Set the styling for all fourth-level headings in your emails. These should be the smallest of your headings.
	   @style heading 4
	   */
	       h4{
	           /*@editable*/color:#808080 !important;
	           display:block;
	           /*@editable*/font-family:'Roboto',Helvetica;
	           /*@editable*/font-size:16px;
	           /*@editable*/font-style:normal;
	           /*@editable*/font-weight:bold;
	           /*@editable*/line-height:125%%%%;
	           /*@editable*/letter-spacing:normal;
	           margin:0;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Preheader
	   @section preheader style
	   @tip Set the background color and borders for your email's preheader area.
	   */
	       #templatePreheader{
	           /*@editable*/background-color:#ffffff;
	           /*@editable*/border-top:0;
	           /*@editable*/border-bottom:0;
	       }
	   /*
	   @tab Preheader
	   @section preheader text
	   @tip Set the styling for your email's preheader text. Choose a size and color that is easy to read.
	   */
	       .preheaderContainer .TextContent,.preheaderContainer .TextContent p{
	           /*@editable*/color:#606060;
	           /*@editable*/font-family:'Roboto',Helvetica;
	           /*@editable*/font-size:11px;
	           /*@editable*/line-height:125%%%%;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Preheader
	   @section preheader link
	   @tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.
	   */
	       .preheaderContainer .TextContent a{
	           /*@editable*/color:#00bcc8;
	           /*@editable*/font-weight:normal;
	           /*@editable*/text-decoration:underline;
	       }
	   /*
	   @tab Header
	   @section header style
	   @tip Set the background color and borders for your email's header area.
	   */
	       #templateHeader{
	           /*@editable*/background-color:#ffffff;
	           /*@editable*/border-top:0;
	           /*@editable*/border-bottom:0;
	       }
	   /*
	   @tab Header
	   @section header text
	   @tip Set the styling for your email's header text. Choose a size and color that is easy to read.
	   */
	       .headerContainer .TextContent,.headerContainer .TextContent p{
	           /*@editable*/color:#606060;
	           /*@editable*/font-family:'Roboto',Helvetica;
	           /*@editable*/font-size:15px;
	           /*@editable*/line-height:150%%%%;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Header
	   @section header link
	   @tip Set the styling for your email's header links. Choose a color that helps them stand out from your text.
	   */
	       .headerContainer .TextContent a{
	           /*@editable*/color:#6DC6DD;
	           /*@editable*/font-weight:normal;
	           /*@editable*/text-decoration:underline;
	       }
	   /*
	   @tab Body
	   @section body style
	   @tip Set the background color and borders for your email's body area.
	   */
	       #templateBody{
	           /*@editable*/background-color:#ffffff;
	           /*@editable*/border-top:0;
	           /*@editable*/border-bottom:0;
	       }
	   /*
	   @tab Body
	   @section body text
	   @tip Set the styling for your email's body text. Choose a size and color that is easy to read.
	   */
	       .bodyContainer .TextContent,.bodyContainer .TextContent p{
	           /*@editable*/color:#606060;
	           /*@editable*/font-family:'Roboto',Helvetica;
	           /*@editable*/font-size:15px;
	           /*@editable*/line-height:150%%%%;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Body
	   @section body link
	   @tip Set the styling for your email's body links. Choose a color that helps them stand out from your text.
	   */
	       .bodyContainer .TextContent a{
	           /*@editable*/color:#6DC6DD;
	           /*@editable*/font-weight:normal;
	           /*@editable*/text-decoration:underline;
	       }
	   /*
	   @tab Footer
	   @section footer style
	   @tip Set the background color and borders for your email's footer area.
	   */
	       #templateFooter{
	           /*@editable*/background-color:#ffffff;
	           /*@editable*/border-top:0;
	           /*@editable*/border-bottom:0;
	       }
	   /*
	   @tab Footer
	   @section footer text
	   @tip Set the styling for your email's footer text. Choose a size and color that is easy to read.
	   */
	       .footerContainer .TextContent,.footerContainer .TextContent p{
	           /*@editable*/color:#606060;
	           /*@editable*/font-family:'Roboto',Helvetica;
	           /*@editable*/font-size:11px;
	           /*@editable*/line-height:125%%%%;
	           /*@editable*/text-align:left;
	       }
	   /*
	   @tab Footer
	   @section footer link
	   @tip Set the styling for your email's footer links. Choose a color that helps them stand out from your text.
	   */
	       .footerContainer .TextContent a{
	           /*@editable*/color:#00bcc8;
	           /*@editable*/font-weight:normal;
	           /*@editable*/text-decoration:underline;
	       }
	   @media only screen and (max-width: 480px){
	       body,table,td,p,a,li,blockquote{
	           -webkit-text-size-adjust:none !important;
	       }

	}   @media only screen and (max-width: 480px){
	       body{
	           width:100%%%% !important;
	           min-width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[id=bodyCell]{
	           padding:10px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       table[class=TextContentContainer]{
	           width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       table[class=BoxedTextContentContainer]{
	           width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       table[class=mcpreview-image-uploader]{
	           width:100%%%% !important;
	           display:none !important;
	       }

	}   @media only screen and (max-width: 480px){
	       img[class=Image]{
	           width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       table[class=ImageGroupContentContainer]{
	           width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageGroupContent]{
	           padding:9px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageGroupBlockInner]{
	           padding-bottom:0 !important;
	           padding-top:0 !important;
	       }

	}   @media only screen and (max-width: 480px){
	       tbody[class=ImageGroupBlockOuter]{
	           padding-bottom:9px !important;
	           padding-top:9px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       table[class=CaptionTopContent],table[class=CaptionBottomContent]{
	           width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       table[class=CaptionLeftTextContentContainer],table[class=CaptionRightTextContentContainer],table[class=CaptionLeftImageContentContainer],table[class=CaptionRightImageContentContainer],table[class=ImageCardLeftTextContentContainer],table[class=ImageCardRightTextContentContainer]{
	           width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageCardLeftImageContent],td[class=ImageCardRightImageContent]{
	           padding-right:18px !important;
	           padding-left:18px !important;
	           padding-bottom:0 !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageCardBottomImageContent]{
	           padding-bottom:9px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageCardTopImageContent]{
	           padding-top:18px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageCardLeftImageContent],td[class=ImageCardRightImageContent]{
	           padding-right:18px !important;
	           padding-left:18px !important;
	           padding-bottom:0 !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageCardBottomImageContent]{
	           padding-bottom:9px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=ImageCardTopImageContent]{
	           padding-top:18px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       table[class=CaptionLeftContentOuter] td[class=TextContent],table[class=CaptionRightContentOuter] td[class=TextContent]{
	           padding-top:9px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=CaptionBlockInner] table[class=CaptionTopContent]:last-child td[class=TextContent]{
	           padding-top:18px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=BoxedTextContentColumn]{
	           padding-left:18px !important;
	           padding-right:18px !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=TextContent]{
	           padding-right:18px !important;
	           padding-left:18px !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section template width
	   @tip Make the template fluid for portrait or landscape view adaptability. If a fluid layout doesn't work for you, set the width to 300px instead.
	   */
	       table[id=templateContainer],table[id=templatePreheader],table[id=templateHeader],table[id=templateBody],table[id=templateFooter]{
	           /*@tab Mobile Styles
	@section template width
	@tip Make the template fluid for portrait or landscape view adaptability. If a fluid layout doesn't work for you, set the width to 300px instead.*/max-width:600px !important;
	           /*@editable*/width:100%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section heading 1
	   @tip Make the first-level headings larger in size for better readability on small screens.
	   */
	       h1{
	           /*@editable*/font-size:24px !important;
	           /*@editable*/line-height:125%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section heading 2
	   @tip Make the second-level headings larger in size for better readability on small screens.
	   */
	       h2{
	           /*@editable*/font-size:20px !important;
	           /*@editable*/line-height:125%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section heading 3
	   @tip Make the third-level headings larger in size for better readability on small screens.
	   */
	       h3{
	           /*@editable*/font-size:18px !important;
	           /*@editable*/line-height:125%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section heading 4
	   @tip Make the fourth-level headings larger in size for better readability on small screens.
	   */
	       h4{
	           /*@editable*/font-size:16px !important;
	           /*@editable*/line-height:125%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section Boxed Text
	   @tip Make the boxed text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	   */
	       table[class=BoxedTextContentContainer] td[class=TextContent],td[class=BoxedTextContentContainer] td[class=TextContent] p{
	           /*@editable*/font-size:18px !important;
	           /*@editable*/line-height:125%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section Preheader Visibility
	   @tip Set the visibility of the email's preheader on small screens. You can hide it to save space.
	   */
	       table[id=templatePreheader]{
	           /*@editable*/display:block !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section Preheader Text
	   @tip Make the preheader text larger in size for better readability on small screens.
	   */
	       td[class=preheaderContainer] td[class=TextContent],td[class=preheaderContainer] td[class=TextContent] p{
	           /*@editable*/font-size:14px !important;
	           /*@editable*/line-height:115%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section Header Text
	   @tip Make the header text larger in size for better readability on small screens.
	   */
	       td[class=headerContainer] td[class=TextContent],td[class=headerContainer] td[class=TextContent] p{
	           /*@editable*/font-size:18px !important;
	           /*@editable*/line-height:125%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section Body Text
	   @tip Make the body text larger in size for better readability on small screens. We recommend a font size of at least 16px.
	   */
	       td[class=bodyContainer] td[class=TextContent],td[class=bodyContainer] td[class=TextContent] p{
	           /*@editable*/font-size:18px !important;
	           /*@editable*/line-height:125%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	   /*
	   @tab Mobile Styles
	   @section footer text
	   @tip Make the body content text larger in size for better readability on small screens.
	   */
	       td[class=footerContainer] td[class=TextContent],td[class=footerContainer] td[class=TextContent] p{
	           /*@editable*/font-size:14px !important;
	           /*@editable*/line-height:115%%%% !important;
	       }

	}   @media only screen and (max-width: 480px){
	       td[class=footerContainer] a[class=utilityLink]{
	           display:block !important;
	       }

	}
	</style>
</head>
<body>
	<center>
		<table align="center" border="0" cellpadding="0" cellspacing="0" id="bodyTable" width="100%%%%">
			<tr>
				<td align="center" id="bodyCell" valign="top">
					<!-- BEGIN TEMPLATE // -->
					<table border="0" cellpadding="0" cellspacing="0" id="templateContainer" width="600">
						
						<tr>
							<td align="center" valign="top">
								<!-- BEGIN HEADER // -->
								<table border="0" cellpadding="0" cellspacing="0" id="templateHeader" width="600">
									<tr>
										<td class="headerContainer" valign="top">
											<table border="0" cellpadding="0" cellspacing="0" class="DividerBlock" width="100%%%%">
												<tbody class="DividerBlockOuter">
													<tr>
														<td class="DividerBlockInner" style="padding: 10px 18px;">
															<table border="0" cellpadding="0" cellspacing="0" class="DividerContent" width="100%%%%">
																<tbody>
																	<tr>
																		<td><span></span></td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
											<table border="0" cellpadding="0" cellspacing="0" class="FollowBlock" width="100%%">
												<tbody class="FollowBlockOuter">
													<tr>
														<td align="center" class="FollowBlockInner" style="padding:9px" valign="top">
															<table border="0" cellpadding="0" cellspacing="0" class="FollowContentContainer" width="100%%">
																<tbody>
																	<tr>
																		<td align="center" style="padding-left:9px;padding-right:9px;">
																			<table border="0" cellpadding="0" cellspacing="0" class="FollowContent" width="100%%">
																				<tbody>
																					<tr>
																						
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
																						
											
										</td>
									</tr>
								</table><!-- // END HEADER -->
							</td>
						</tr>
						<tr>
							<td align="center" valign="top">
								<!-- BEGIN BODY // -->
								<table border="0" cellpadding="0" cellspacing="0" id="templateBody" width="600">
									<tr>
										<td class="bodyContainer" valign="top">
											<table border="0" cellpadding="0" cellspacing="0" class="ButtonBlock" width="100%%">
												<tbody class="ButtonBlockOuter">
													<tr>
														<td align="center" class="ButtonBlockInner" style="padding-top:0; padding-right:18px; padding-bottom:18px; padding-left:18px;" valign="top">
															<table border="0" cellpadding="0" cellspacing="0" class="ButtonContentContainer" style="border-collapse: separate !important;border-radius: 5px;">
																<tbody>
																	<tr>
																		<td align="center" class="logo" style="font-family: 'Roboto',Arial; font-size: 16px; padding: 16px;" valign="middle"><img align="left" alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/g-trans_logo.png" style="max-width:1200px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" width="200"> 
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
											<table border="0" cellpadding="0" cellspacing="0" class="TextBlock" width="100%%">
												<tbody class="TextBlockOuter">
													<tr>
														<td class="TextBlockInner" valign="top">
															<table align="left" border="0" cellpadding="0" cellspacing="0" class="TextContentContainer" width="600">
																<tbody>
																	<tr>
																		<td class="TextContent" style="padding-top:9px; padding-right: 18px; padding-bottom: 9px; padding-left: 18px;" valign="top">
																			<div style="text-align: center;">
																				<span style="font-family:'Roboto', arial,helvetica neue,helvetica,sans-serif"><span style="font-size:39px"><span style="color:#00bcc8"><strong>GTrans News Letter</strong></span></span><br>
																				<br>
																				<span style="color:#697b7c"><span style="font-size:14px; line-height:14px; text-align:justify">We are a logistics service provider company to various Multinational and Indian Companies of repute since inception of 5 years of our operation into logistics. We have been able to provide solution to optimize the total supply chain management.<br/><br/> We are transforming the antiquated logistics industry and bringing it into the 21st century with the help of latest technology.</span></span></span>
																			</div>
																		</td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
											<table border="0" cellpadding="0" cellspacing="0" class="DividerBlock" width="100%%">
												<tbody class="DividerBlockOuter">
													<tr>
														<td class="DividerBlockInner" style="padding: 20px 18px 0px;">
															<table border="0" cellpadding="0" cellspacing="0" class="DividerContent" width="100%%">
																<tbody>
																	<tr>
																		<td><span></span></td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
											
											<table border="0" cellpadding="0" cellspacing="0" class="ImageBlock" width="100%%">
												<tbody class="ImageBlockOuter">
													<tr>
														<td class="ImageBlockInner" style="padding:0px" valign="top">
															<table align="left" border="0" cellpadding="0" cellspacing="0" class="ImageContentContainer" width="100%%">
																<tbody>
																	<tr>
																		<td class="ImageContent" style="padding-right: 0px; padding-left: 0px; padding-top: 0; padding-bottom: 0;" valign="top"><img align="left" alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/5109c8dc-8312-49c1-a63a-913aae5410b4.png" style="max-width:1200px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" width="600"></td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
											<table border="0" cellpadding="0" cellspacing="0" class="CaptionBlock" width="100%%">
												<tbody class="CaptionBlockOuter">
													<tr>
														<td class="CaptionBlockInner" style="padding:9px;" valign="top">
															<table border="0" cellpadding="0" cellspacing="0" class="CaptionRightContentOuter" width="100%%">
																<tbody>
																	<tr>
																		<td class="CaptionRightContentInner" style="padding:0 9px ;" valign="top">
																			<table align="center" border="0" cellpadding="0" cellspacing="0" class="CaptionRightImageContentContainer">
																				<tbody>
																					<tr>
																						<td valign="top" align="center"><img alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/merger.png" style="max-width:1200px;" width="600"></td>
																					</tr>
																				</tbody>
																			</table>
																			<table align="center" border="0" cellpadding="0" cellspacing="0" class="CaptionRightTextContentContainer" width="600">
																				<tbody>
																					<tr>
																						<td class="TextContent" style="text-align: center;" valign="top"><span style="font-size:24px"><strong><span style="color:#474747">Merger of Gtrans & Moovo</span></strong></span><br>
																						<br>
																						<span style="color:#697b7c;font-size:14px">
																							We are pleased to announce that Gtrans Logistics and Moovo, owners of a leading logistics company and tech enable losgistics startup respectively, have signed an agreement to merge together. This merger will strengthen to integrate techonology and become a leading technology enabled logistics solution & services provider to Multinational and Indian Companies of repute.

																							<br/>
								
																							<br/>

																							The dynamic Moovo team members has joined our team and started working together to fulfill our company goal <i>"Your Success Our Logistics"</i> 

																							<br/>
																							<br/>

																							This merged entity will be administered by <i><b>"Mr Gagan Chaturvedi"</b></i><br/>

																										<br/>

																									For More Information
																									<br/>

																							          <b>(M).</b> 8800492569 <b>E-mail:</b> info@g-translogistics.com <b>Website: </b>www.g-translogistics.com

																						</span></td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>

											
											<table border="0" cellpadding="0" cellspacing="0" class="ImageBlock" width="100%%">
												<tbody class="ImageBlockOuter">
													<tr>
														<td class="ImageBlockInner" style="padding:0px" valign="top">
															<table align="left" border="0" cellpadding="0" cellspacing="0" class="ImageContentContainer" width="100%%">
																<tbody>
																	<tr>
																		<td class="ImageContent" style="padding-right: 0px; padding-left: 0px; padding-top: 0; padding-bottom: 0;" valign="top"><img align="left" alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/5109c8dc-8312-49c1-a63a-913aae5410b4.png" style="max-width:1200px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" width="600"></td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>

											<table border="0" cellpadding="0" cellspacing="0" class="CaptionBlock" width="100%%">
												<tbody class="CaptionBlockOuter">
													<tr>
														<td class="CaptionBlockInner" style="padding:9px;" valign="top">
															<table border="0" cellpadding="0" cellspacing="0" class="CaptionRightContentOuter" width="100%%">
																<tbody>
																	<tr>
																		<td class="CaptionRightContentInner" style="padding:0 9px ;" valign="top">
																			<table border="0" cellpadding="0" cellspacing="0" class="" align="center" style="border-collapse: separate !important;border-radius: 5px;">
																				<tbody>
																					<tr>
																						<td align="center" class="logo" style="font-family: 'Roboto',Arial; font-size: 16px; padding: 16px;" valign="middle"><img align="left" alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/G-TechLogoV03.png" style="max-width:1200px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" width="300"> 
																					</tr>
																				</tbody>
																			</table>
																			<table align="center" border="0" cellpadding="0" cellspacing="0" class="CaptionRightImageContentContainer">
																				<tbody>
																					<tr>
																						<td class="CaptionRightImageContent" valign="top"><img alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/gtechV02.png" style="max-width:1200px;" width="600"></td>
																					</tr>
																				</tbody>
																			</table>
																			
																			<table align="center" border="0" cellpadding="0" cellspacing="0" class="CaptionRightTextContentContainer" width="600">
																				<tbody>
																					<tr>
																						<td class="TextContent" valign="top" style="text-align: center;"><span style="font-size:24px "><strong><span style="color:#474747">G Tech Solutions</span></strong></span><br>
																						<br>
																						<span style="color:#697b7c;font-size:14px">G Tech Solutions is a fast growing brand ventured by a passionate team from world’s most eminent institutions. We are dedicated to the field of GPS based vehicle tracking solutions and its exhaustive data analytics. Proficient in providing valuable solutions, we cater to diverse clients from all verticals. Our aim is to set benchmarks in GPS industry in terms of imparting avant-garde solutions, high quality services, and ceaseless support to our customers.

																						<br/>
																							<br/>

																							This entity will be administered by <i><b>"Mr Harshit Sinha"</b></i><br/>
																							<br/>

																									For More Information
																									<br/>

																							          <b>(M).</b> 7838850643 <b>E-mail:</b> info@g-techsolutions.in<b> Website: </b>www.track.gogeotrack.com

																						</span></td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
											<table border="0" cellpadding="0" cellspacing="0" class="ImageBlock" width="100%%">
												<tbody class="ImageBlockOuter">
													<tr>
														<td class="ImageBlockInner" style="padding:9px" valign="top">
															<table align="left" border="0" cellpadding="0" cellspacing="0" class="ImageContentContainer" width="100%%">
																<tbody>
																	<tr>
																		<td class="ImageContent" style="padding-right: 9px; padding-left: 9px; padding-top: 0; padding-bottom: 0;" valign="top"><img align="left" alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/5109c8dc-8312-49c1-a63a-913aae5410b4.png" style="max-width:1200px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" width="564"></td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>

											<table border="0" cellpadding="0" cellspacing="0" class="CaptionBlock" width="100%%">
												<tbody class="CaptionBlockOuter">
													<tr>
														<td class="CaptionBlockInner" style="padding:9px;" valign="top">
															<table border="0" cellpadding="0" cellspacing="0" class="CaptionRightContentOuter" width="100%%">
																<tbody>
																	<tr>
																		<td class="CaptionRightContentInner" style="padding:0 9px ;" valign="top">

																			<table border="0" cellpadding="0" cellspacing="0" class="" align="center" style="border-collapse: separate !important;border-radius: 5px;">
																				<tbody>
																					<tr>
																						<td align="center" class="logo" style="font-family: 'Roboto',Arial; font-size: 16px; padding: 16px;" valign="middle"><img align="left" alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/Gap_Logo.png" style="max-width:1200px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" width="300"> 
																					</tr>
																				</tbody>
																			</table>

																			<table align="center" border="0" cellpadding="0" cellspacing="0" class="CaptionRightImageContentContainer">
																				<tbody>
																					<tr>
																						<td class="CaptionRightImageContent" valign="top" ><img alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/gap_logix_port.png" style="max-width:1200px;"  width="600"></td>
																					</tr>
																				</tbody>
																			</table>
																			
																			<table align="center" border="0" cellpadding="0" cellspacing="0" class="CaptionRightTextContentContainer" width="600">
																				<tbody>
																					<tr>
																						<td class="TextContent" style="text-align: center;" valign="top"><span style="font-size:24px"><strong><span style="color:#474747">We Create Experience</span></strong></span><br>
																						<br>
																						<span style="color:#697b7c;font-size:14px">Gaplogix long term philosophy and goals are best reflected by our purpose of <i>"We Create Experience"</i>. We focus on people, processes and technology to enhance business productivity by enabling our clients to outsource their staffing requirements and allowing them to focus on operating and growing their core businesses.
																						<br/>
																							<br/>

																							This entity will be administered by <i><b>"Mrs Preeti Chakrabortty"</b></i><br/>
																							<br/>

																									For More Information
																									<br/>

																							          <b>(M).</b> 8800591427<b> E-mail:</b> info@gaplogix.com<b> Website: </b>www.gaplogix.com


																						</span></td>
																					</tr>
																				</tbody>
																			</table>
																		</td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
											
											
											
											
											
											
											<table border="0" cellpadding="0" cellspacing="0" class="ImageBlock" width="100%%">
												<tbody class="ImageBlockOuter">
													<tr>
														<td class="ImageBlockInner" style="padding:0px" valign="top">
															<table align="left" border="0" cellpadding="0" cellspacing="0" class="ImageContentContainer" width="100%%">
																<tbody>
																	<tr>
																		<td class="ImageContent" style="padding-right: 0px; padding-left: 0px; padding-top: 0; padding-bottom: 0;" valign="top"><img align="left" alt="" class="Image" src="http://alpha.gtrans-admin.appspot.com/images/news/5109c8dc-8312-49c1-a63a-913aae5410b4.png" style="max-width:1200px; padding-bottom: 0; display: inline !important; vertical-align: bottom;" width="600"></td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
										</td>
									</tr>
								</table><!-- // END BODY -->
							</td>
						</tr>
						<tr>
							<td align="center" valign="top">
								<!-- BEGIN FOOTER // -->
								<table border="0" cellpadding="0" cellspacing="0" id="templateFooter" width="600">
									<tr>
										<td class="footerContainer" style="padding-bottom:9px;" valign="top">
											<table border="0" cellpadding="0" cellspacing="0" class="TextBlock" width="100%%">
												<tbody class="TextBlockOuter">
													<tr>
														<td class="TextBlockInner" valign="top">
															<table align="left" border="0" cellpadding="0" cellspacing="0" class="TextContentContainer" width="600">
																<tbody>
																	<tr>
																		<td class="TextContent" style="padding-top:9px; padding-right: 18px; padding-bottom: 9px; padding-left: 18px;" valign="top">
																			<div style="text-align: center;">
																				You are receiving this email because you signed up at our website.&nbsp;If you want to unsubscribe, <a href="#" target="_self">click here</a>.<br>
																				<br>
																				<span style="color:#697b7c">Designed by</span> <a href="http://www.g-translogistics.com" target="_blank">Gtrans</a>
																			</div>
																		</td>
																	</tr>
																</tbody>
															</table>
														</td>
													</tr>
												</tbody>
											</table>
										</td>
									</tr>
								</table><!-- // END FOOTER -->
							</td>
						</tr>
					</table><!-- // END TEMPLATE -->
				</td>
			</tr>
		</table>
	</center>
</body>
</html>'''