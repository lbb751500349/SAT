$(function(){
    $(".checkall").change(function(){
        console.log($(".checkall").prop("checked"))
        $(".check-j, .checkall").prop("checked", $(".checkall").prop("checked"))
    })
    $(".check-j").change(function(){
        console.log($(".check-j:checked").length)
        if ($(".check-j:checked").length === $(".check-j").length){
            $(".checkall").prop("checked", true)
        }else{
            $(".checkall").prop("checked", false)
        }

    })

})