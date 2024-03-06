<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@include file="/jsp/common/head.jsp"%>

<div class="right">
     <div class="location">
         <strong>你现在所在的位置是:</strong>
         <span>订单管理页面 >> 订单添加页面</span>
     </div>
     <div class="providerAdd">
         <form id="billForm" name="billForm" method="post" action="${pageContext.request.contextPath }/jsp/bill.do">
             <!--div的class 为error是验证错误，ok是验证成功-->
             <input type="hidden" name="method" value="add">
             <div class="">
                 <label for="billCode">订单编码：</label>
                 <input type="text" name="billCode" class="text" id="billCode" value=""> 
				 <!-- 放置提示信息 -->
				 <font color="red"></font>
             </div>
             <div>
                 <label for="productName">商品名称：</label>
                 <input type="text" name="productName" id="productName" value=""> 
				 <font color="red"></font>
             </div>
             <div>
                 <label for="productUnit">商品单位：</label>
                 <input type="text" name="productUnit" id="productUnit" value=""> 
				 <font color="red"></font>
             </div>
             <div>
                 <label for="productCount">商品数量：</label>
                 <input type="text" name="productCount" id="productCount" value=""> 
				 <font color="red"></font>
             </div>
             <div>
                 <label for="totalPrice">总金额：</label>
                 <input type="text" name="totalPrice" id="totalPrice" value=""> 
				 <font color="red"></font>
             </div>
             <div>
                 <label >供应商：</label>
                 <select name="providerId" id="providerId">
                     <option value="0">--请选择--</option>
                     <option value="1">北京三木堂商贸有限公司</option>
                     <option value="2">石家庄帅益食品贸易有限公司</option>
                     <option value="3">深圳市泰香米业有限公司</option>
                     <option value="4">深圳市喜来客商贸有限公司</option>
                     <option value="5">兴化佳美调味品厂</option>
                     <option value="6">北京纳福尔食用油有限公司</option>
                     <option value="7">北京国粮食用油有限公司</option>
                     <option value="8">慈溪市广和绿色食品厂</option>
                     <option value="9">优百商贸有限公司</option>
                     <option value="10">南京火头军信息技术有限公司</option>
                     <option value="11">广州市白云区美星五金制品厂</option>
                     <option value="12">北京隆盛日化科技</option>
                     <option value="13">山东豪克华光联合发展有限公司</option>
                     <option value="14">无锡喜源坤商行</option>
                     <option value="15">乐摆日用品厂</option>
                 </select>
				 <font color="red"></font>
             </div>
             <div>
                 <label >是否付款：</label>
                 <input type="radio" name="isPayment" value="1" checked="checked">未付款
				 <input type="radio" name="isPayment" value="2" >已付款
             </div>
             <div class="providerAddBtn">
                  <input type="button" name="add" id="add" value="保存">
				  <input type="button" id="back" name="back" value="返回" >
             </div>
         </form>
     </div>
 </div>
</section>
<%@include file="/jsp/common/foot.jsp" %>
<script type="text/javascript" src="${pageContext.request.contextPath }/js/billadd.js"></script>