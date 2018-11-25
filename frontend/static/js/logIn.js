$(function() {
	//禁止滚动条
	$(document.body).css({
		"overflow-x": "hidden",
	});

	/*========================================================
	         更改密码表单验证（pCenter.html + pCenterProject.heml 更改密码使用）
    ==========================================================*/
	//密码验证规则
	/*$.validator.addMethod('pass', function(value, element) {
		var pass = /^[\w]+$/
		return this.optional(element) || (pass.test(value));
	});*/
	$("#changePasswordForm").validate({
		submitHandler: function(form) {
			$('#changePasswordSuccessIndicator').css('display', 'block');
			//对比旧密码和数据库里面的密码是否一致
			///////////////////////////////////
			//$('#changePasswordErrorIndicator').css('display','block');
		}
	});
	//旧密码
	$("#oldPassword").rules('add', {
		required: true,
		messages: {
			required: 'The current password cannot be empty！'
		}
	});
	//新密码
	$("#newPassword").rules('add', {
		required: true,
		minlength: 6,
		maxlength: 20,
		pass: true,
		messages: {
			required: 'Please enter 6-20 digits, numbers and letters！',
			minlength: 'Password cannot be less than {0} bits！',
			maxlength: 'Password cannot exceed {0} bit！',
			pass: 'Password cannot contain symbols other than numbers and letters！'
		}
	});
	//确认密码
	$("#repeatPassword").rules('add', {
		required: true,
		equalTo: '#newPassword',
		messages: {
			required: 'Please enter your password again',
			equalTo: 'Inconsistent password entry',
		}
	});

	/*========================================================
	        创建项目 + 修改项目名称 验证表单以及
	        动态添加项目（pCenter.html 使用）
    ==========================================================*/
	//创建项目
	$("#createProjectForm").validate({
		submitHandler: function(form) {
			var v = $('#createProjectName').val();
			var i = $('#newProject li').length + 1;
			var nameId="pjName"+i;
			var dateId="pjCreatedDate"+i;
			var numId="pjNum"+i;

			$('#createProjectModal').modal('hide');
			var d1 = "<li class='col-md-4 col-lg-4 col-sm-4 col-xs-6 project-12'><div class='projectCard'>" +
				" <div class = 'projectFolderImage' ><div class = 'projectFolderBG'> </div>" +
				" <div class = 'numServices'> <span id=" + numId + "> 0 张图像码 </span></div> " +
				" <h3 class = 'projectName'><span id=" + nameId + "></span></h3> " +
				"<p class = 'projectDescription truncate' ></p>" +
				" <div class = 'projectOptions' >" +
				" <a href = '#' class='editProject pencil-img' data-toggle = 'modal' data-target = '#editProjectModal' > </a>" +
				" <a href = '#' > &nbsp; </a>" +
				" <a href = '#' class='deleteProject delete-img' data-toggle = 'modal' data-target = '#deleteProjectModal' > </a>" +
				" </div> <a href = 'pCenterProject.html' class = 'next-arrow'> </a>" +
				" </div><span class='projectDate' id=" + dateId + "></span> " +
				" </div> </li>";

				//创建日期
			var date = new Date();
			var str = "创建日期：" + date.getFullYear()
                + "-"
                + ((date.getMonth() + 1) > 10 ? (date.getMonth() + 1) : "0"+(date.getMonth() + 1))
                + "-"
                + (date.getDate() < 10 ? "0"+date.getDate() : date.getDate());

			$("#newProject").append(d1);
			$('#'+nameId).html(v);
			$('#'+dateId).html(str);
		}
	});
	$("#createProjectName").rules('add', {
		required: true,
		messages: {
			required: '请输入项目名称！'
		}
	});

	//修改名称
	$("#editProjectForm").validate({
		submitHandler: function(form) {
//			var v = $('#projectName').val();
//			var i=2;
//			var nowId="pjName"+ i;
//			$('#'+newId).html(v);
		}
	});
	$("#projectName").rules('add', {
		required: true,
		messages: {
			required: '请输入项目名称！'
		}
	});

	/*========================================================
	            账户设置下各表单验证（accountSettings.html 使用）
    ========================================================*/
	$("#accountSettingsForm").validate({
		submitHandler: function(form) {}
	});
	//邮箱
	$("#email_account").rules('add', {
		required: true,
		email: true,
		messages: {
			required: '请输入您的邮箱！',
			email: '请输入正确的邮箱！',
		}
	});
	//用户名
	$("#username").rules('add', {
		required: true,
		minlength: 6,
		maxlength: 40,
		messages: {
			required: '请输入不少于6位的用户名/公司名',
			minlength: '不能小于{0}个字母或者数字！',
			maxlength: '不能超过{0}字母或者数字！',
			pass: '用户名不能含数字和字母以外的符号！'
		}
	});
	//联系电话
	$("#phone").rules('add', {
		minlength: 11,
		isMobile: true,
		messages: {
			minlength: "手机号码不能小于11个字符 ",
			isMobile: "请正确填写您的手机号码 "
		}
	});

	$("#cardInfo").validate({
		submitHandler: function(form) {}
	});

	//用户名
	$("#cardHolderName").rules('add', {
		required: true,
		messages: {
			required: '请输入真实姓名'
		}
	});
	//联系电话
	$("#truePhone").rules('add', {
		required: true,
		minlength: 11,
		isMobile: true,
		messages: {
			required: "请输入联系电话",
			minlength: "手机号码不能小于11个字符 ",
			isMobile: "请正确填写您的手机号码 "
		}
	});
	//身份证
	$("#idCardNumber").rules('add', {
		required: true,
		isIdCardNo: true,
		messages: {
			required: "请填写您的身份证号码",
			isIdCardNo: "请正确输入您的身份证号码 "
		}
	});
	//银行卡
	$("#creditCardNumber").rules('add', {
		required: true,
		isCreditCardNo: true,
		messages: {
			required: "请填写您的银行卡号",
			isCreditCardNo: "请正确填写您的银行卡号 "
		}
	});

	/*========================================================
	               登录注册表单验证（logInAndSignUp.html 使用）
    ========================================================*/
	$("#logIn-form").validate();
	//邮箱
	$("#email").rules('add', {
		required: true,
		email: true,
		messages: {
			required: 'Please enter your email！',
			email: 'Please enter your correct email！',
		}
	});
	//密码
	$("#password").rules('add', {
		required: true,
		minlength: 6,
		maxlength: 20,
		pass: true,
		messages: {
			required: 'Please enter 6-20 digits, numbers and letters！',
			minlength: 'Password cannot be less than {0} bits！',
			maxlength: 'Password cannot exceed {0} bit！',
			pass: 'Password cannot contain symbols other than numbers and letters！'
		}
	});
	// 邮箱自动补全
	$("#email").autocomplete({
		delay: 0,
		//autoFoucs:true,
		source: function(request, response) {
			var hosts = ['qq.com', '163.com', '126.com', 'sina.com.cn', '263.com'],
				term = request.term, //获取用户输入的内容
				name = term, //邮箱的用户名
				host = '', //邮箱的域名
				ix = term.indexOf('@'), //@的位置
				result = [];

			//当有@的时候，重新分配用户名和域名
			if(ix > -1) {
				name = term.slice(0, ix);
				host = term.slice(ix + 1);
			}
			if(name) {
				//如果用户已经输入@和后面的域名，
				//那么就找到相关的提示，比如bnbbs@1,就提示bnbbs@163.com
				//如果用户还没有输入@，那就提示所有域名
				var findedHosts = [];
				if(host) {
					findedHosts = $.grep(hosts, function(value, index) {
						return value.indexOf(host) > -1
					});
				} else {
					findedHosts = hosts;
				}
				var findedResult = $.map(findedHosts, function(value, index) {
					return name + '@' + value;
				})
				if(findedResult == '') {
					result.push(term)
				}

				result = result.concat(findedResult);
			}
			response(result);
		}
	});

	/*========================================================
	               个人用户注册（logInAndSignUp.html 使用）
    ========================================================*/
	$("#accountPersonalRegisterForm").validate({
		submitHandler: function(form) {

			$('#registerPersonalModal').modal('hide');
			$('#registerSuccessModal').modal('toggle');
			$('#registerSuccessModal').modal('show');
			$("#confirmregisterEmailAddressSpan").html($("#rpEmailAddress").val());
			var myform = $(form),
			email = myform.find( "input[name='email']" ).val(),
			username = myform.find( "input[name='username']" ).val(),
			currentpassord = myform.find( "input[name='currentPassword']" ).val(),
			url = myform.attr("action" );
			// Send the data using post
			var posting = $.post(url, {'email': email,'username': username,'currentPassword':currentpassord});
		}
	});
	//邮箱
	$("#rpEmailAddress").rules('add', {
		required: true,
		email: true,
		messages: {
			required: 'Please enter your email！',
			email: 'Please enter your correct email！',
		}
	});
	//密码
	$("#rpCurrentPassword").rules('add', {
		required: true,
		minlength: 6,
		maxlength: 20,
		pass: true,
		messages: {
			required: 'Please enter 6-20 digits, numbers and letters！',
			minlength: 'Password cannot be less than {0} bits！',
			maxlength: 'Password cannot exceed {0} bit！',
			pass: 'Password cannot contain symbols other than numbers and letters！'
		}
	});
	//确认密码
	$("#rpConfirmPassword").rules('add', {
		required: true,
		equalTo: '#rpCurrentPassword',
		messages: {
			required: 'Please enter your password again',
			equalTo: 'Inconsistent password entry',
		}
	});
	// 协议
	$("#acceptP").rules('add', {
		required: true,
		messages: {
			required: 'Please accept the registration agreement！'
		},
		highlight: function(element, errorClass) {
			setTimeout(function() {
				if($("#acceptP-error").get(0)) {
					$("#acceptP-error").css("display", "block")
					$(".accept-p").insertBefore("#acceptP-error");

				}
			}, 0);
		},
	});

	/*========================================================
	               官方用户注册（logInAndSignUp.html 使用）
    ========================================================*/
	$("#accountBusinessRegisterForm").validate({
		submitHandler: function(form) {
			$('#registerBusinessModal').modal('hide');
			$('#registerSuccessModal').modal('toggle');
			$('#registerSuccessModal').modal('show');
			$("#confirmregisterEmailAddressSpan").html($("#rbEmailAddress").val());
		}
	});
	//邮箱
	$("#rbEmailAddress").rules('add', {
		required: true,
		email: true,
		messages: {
			required: '请输入您的邮箱！',
			email: '请输入正确的邮箱！',
		}
	});
	//密码
	$("#rbCurrentPassword").rules('add', {
		required: true,
		minlength: 6,
		maxlength: 20,
		pass: true,
		messages: {
			required: '请输入6-20位密码，数字和字母！',
			minlength: '密码不能小于{0}位！',
			maxlength: '密码不能超过{0}位！',
			pass: '密码不能含数字和字母以外的符号！'
		}
	});
	//确认密码
	$("#rbConfirmPassword").rules('add', {
		required: true,
		equalTo: '#rbCurrentPassword',
		messages: {
			required: '请再次输入密码',
			equalTo: '密码输入不一致',
		}
	});
	// 协议
	$("#acceptB").rules('add', {
		required: true,
		messages: {
			required: '请接受官方用户注册协议！'
		},
		highlight: function(element, errorClass) {
			setTimeout(function() {
				if($("#acceptB-error").get(0)) {
					$("#acceptB-error").css("display", "block")
					$(".accept-b").insertBefore("#acceptB-error");

				}
			}, 0);
		},
	});

	/*========================================================
	         更改密码表单验证（logInAndSignUp.html 使用）
    ========================================================*/
	/*邮箱实时验证*/
	$("#resetPasswordForm").validate({
		submitHandler: function(form) {}
	});
	//邮箱
	$("#forgotPasswordEmail").rules('add', {
		required: true,
		email: true,
		messages: {
			required: '请输入您的邮箱！',
			email: '请输入正确的邮箱！',
		}
	});
	//提交邮箱验证
	$("#submitForgotPasswordBtn").click(function() {
		var reg = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
		if(reg.test($("#forgotPasswordEmail").val())) {
			$('#forgotPasswordModal').modal('hide');
			$('#resetSuccessModal').modal('toggle');
			$('#resetSuccessModal').modal('show');
			$("#forgotPasswordEmailSpan").html($("#forgotPasswordEmail").val());
		}
	});

	/*========================================================
	             自定义验证方法
    ========================================================*/
	//邮箱验证规则
	$.validator.addMethod('email', function(value, element) {
		var email = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+((\.[a-zA-Z0-9_-]{2,3}){1,2})$/;
		return this.optional(element) || (email.test(value));
	});
	//手机号码验证
	$.validator.addMethod('isMobile', function(value, element) {
		var length = value.length;
		var mobile = /^(13[0-9]{9})|(18[0-9]{9})|(14[0-9]{9})|(17[0-9]{9})|(15[0-9]{9})$/;
		return this.optional(element) || (length == 11 && mobile.test(value));
	});
	//身份证验证规则
	$.validator.addMethod('isIdCardNo', function(value, element) {
		var idCardNo = /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/;
		return this.optional(element) || idCardNo.test(value);
	});
	//银行卡验证规则
	$.validator.addMethod('isCreditCardNo', function(value, element) {
		var creditCardNo = /^(\d{16}|\d{19})$/;
		return this.optional(element) || creditCardNo.test(value);
	});
	//密码验证规则
	$.validator.addMethod('pass', function(value, element) {
		var pass = /^[\w]+$/
		return this.optional(element) || (pass.test(value));
	});

	/*=========================================================================
		全局错误提醒
	=========================================================================*/
	$.validator.setDefaults({
		highlight: function(element, errorClass) {
			$(element).parents('.form-group').removeClass('has-success has-feedback');
			$(element).parents('.form-group').addClass('has-error has-feedback');
			if($(element).parents('.form-group').find("span:empty").prev().prop('tagName') != 'I') {
				$(element).parents('.form-group').find("span:empty").removeClass('glyphicon glyphicon-ok form-control-feedback');
				$(element).parents('.form-group').find("span:empty").addClass('glyphicon glyphicon-exclamation-sign form-control-feedback');
			} else if($(element).parents('.form-group').find("span:empty").prev().prop('tagName') == 'I') {
				$(element).parents('.form-group').find("i").show();
				$(element).parents('.form-group').find("span:empty").hide();
			}
			setTimeout(function() {
				$(element).parent().find("label").addClass('control-label');
			}, 0);
		},
		unhighlight: function(element, errorClass) {
			$(element).parents('.form-group').removeClass('has-error has-feedback');
			$(element).parents('.form-group').addClass('has-success has-feedback');
			if($(element).parents('.form-group').find("span:empty").prev().prop('tagName') != 'I') {
				$(element).parents('.form-group').find("span:empty").removeClass('glyphicon glyphicon-exclamation-sign form-control-feedback');
				$(element).parents('.form-group').find("span:empty").addClass('glyphicon glyphicon-ok form-control-feedback');
			} else if($(element).parents('.form-group').find("span:empty").prev().prop('tagName') == 'I') {
				$(element).parents('.form-group').find("i").hide();
				$(element).parents('.form-group').find("span:empty").addClass('glyphicon glyphicon-ok form-control-feedback').show();
			}
		},
		focusInvalid: false,
	});

	/*=========================================================================
		密码眼睛关闭睁开
	=========================================================================*/
	/*$("i.glyphicon").click(function(){
	    if($(this).hasClass("glyphicon-eye-close")){
	        $(this).removeClass("glyphicon-eye-close").addClass('glyphicon-eye-open');
	        $(this).parent().find("input").prop("type","text")
	    }
	    else{
	        $(this).removeClass("glyphicon-eye-open").addClass('glyphicon-eye-close');
	         $(this).parent().find("input").prop("type","password")
	    }
	});*/

	/*=========================================================================
		日期选择
	=========================================================================*/
	/*if($("#birthday").get(0)) {
		jeDate({
			dateCell: "#birthday",
			format: "YYYY-MM-DD",
			minDate: "1900-1-1",
			maxDate: jeDate.now(0),
			ishmsVal: false,
		});
	};

	$("#birthday").one('blur', function() {
		$(this).focus();
	});

	$("#birthday").trigger("click");
	$("body").trigger("click");*/

})
